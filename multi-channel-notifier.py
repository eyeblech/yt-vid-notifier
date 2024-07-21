import requests
import json
import time
import os

# Configuration
YOUTUBE_API_KEY = 'YOUR_YT_API'
CHANNEL_IDS = [
    'channel_id_1',
    'channel_id_2',
    'channel_id_3',
    'channel_id_4',
    'channel_id_5'
]
WEBHOOK_URL = 'WEBHOOK_URL'
CHECK_INTERVAL = 60 * 15  # Check every 15 minutes
LAST_VIDEO_IDS_FILE = 'last_video_ids.json'

def load_last_video_ids():
    if os.path.exists(LAST_VIDEO_IDS_FILE):
        with open(LAST_VIDEO_IDS_FILE, 'r') as file:
            return json.load(file)
    return {channel_id: None for channel_id in CHANNEL_IDS}

def save_last_video_ids(last_video_ids):
    with open(LAST_VIDEO_IDS_FILE, 'w') as file:
        json.dump(last_video_ids, file)

def get_latest_video(channel_id):
    url = f"https://www.googleapis.com/youtube/v3/search?key={YOUTUBE_API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            video_id = data["items"][0]["id"].get("videoId")
            title = data["items"][0]["snippet"]["title"]
            return video_id, title
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 403:
            print(f"Error fetching data from YouTube API for channel {channel_id}: 403 Forbidden - Check your API key permissions and quota.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None, None

def send_discord_message(video_id, title):
    data = {
        "content": f"New video from the channel: [{title}](https://www.youtube.com/watch?v={video_id})"
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        print("Notification sent to Discord.")
    except requests.RequestException as e:
        print(f"Failed to send notification: {e}")

def main():
    last_video_ids = load_last_video_ids()
    while True:
        for channel_id in CHANNEL_IDS:
            video_id, title = get_latest_video(channel_id)
            if video_id and video_id != last_video_ids[channel_id]:
                send_discord_message(video_id, title)
                last_video_ids[channel_id] = video_id
                save_last_video_ids(last_video_ids)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
