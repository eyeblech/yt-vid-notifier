# Intro

"Simple Python script to get notified about the latest YouTube video from any specific channel that you prefer on Discord!"

# Getting Started


## Step 1: Set up YouTube Data API

* Go to the Google Cloud Console.

* Create a new project (or select an existing one).

* Enable the YouTube Data API v3 for your project.

* Create API credentials (API key).

## Step 2: Set up a Discord Webhook
* Open your Discord server.

* Go to Server Settings > Integrations > Webhooks.

* Click "New Webhook" and customize it as you like.

* Copy the Webhook URL.

## Set Up Python Environment
* Install Python: Make sure Python is installed on your system. You can download it from the official Python website.

* Install Required Libraries: You'll need the 'requests' library to make HTTP requests. You can install it using pip:

```sh
pip install requests
```
* Create the Python Script

* Create a New File: Open your favorite text editor or an Integrated Development Environment (IDE) like VS Code, PyCharm, or any other.

* Save the Script: Copy the provided script and save it as `yt-vid-notifier.py`

* Replace Placeholder Values

  Open the `yt-vid-notifier.py` file and replace

  `YOUR_YOUTUBE_API_KEY`, `TARGET_CHANNEL_ID`, and 
  `YOUR_DISCORD_WEBHOOK_URL`

## Running On a Cloud Instance

* The Program is meant to run every 15 minutes and check for a new video , inorder to do that run it on a cloud server 
* You can use Google Console , AWS or Heroku e.t.c
* "Instead, you choose to run it locally, create a cron job so that it can automatically run at specified intervals of time."

```sh
crontab -e
```
```sh
0 */8 * * * /usr/bin/python /home/samsep10l/Desktop/yt-vid-notifier.py
```

* to list cron jobs
```sh
crontab -l
```

## Proof Of Concept

![py-yt](https://github.com/user-attachments/assets/159152ab-ae84-425c-af58-b7ccceeb95aa)

![yt-notified](https://github.com/user-attachments/assets/8402d992-af40-4911-a5de-6d4fae6329da)


