import requests
import json
import time

# Configuration
YOUTUBE_API_KEY = 'your_api'
CHANNEL_ID = 'channel_id'
WEBHOOK_URL = 'your_webhook_here'
CHECK_INTERVAL = 60 * 15  # Check every 15 minutes

def get_latest_video():
    url = f"https://www.googleapis.com/youtube/v3/search?key={YOUTUBE_API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            video_id = data["items"][0]["id"]["videoId"]
            title = data["items"][0]["snippet"]["title"]
            return video_id, title
    return None, None

def send_discord_message(video_id, title):
    data = {
        "content": f"New video from the channel: [{title}](https://www.youtube.com/watch?v={video_id})"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers)
    if response.status_code == 204:
        print("Notification sent to Discord.")
    else:
        print(f"Failed to send notification: {response.status_code}")

def main():
    last_video_id = None
    while True:
        video_id, title = get_latest_video()
        if video_id and video_id != last_video_id:
            send_discord_message(video_id, title)
            last_video_id = video_id
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()

