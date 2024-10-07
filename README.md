# YouTube Video Downloader and Google Drive Uploader

This script allows you to download a YouTube video and upload it directly to your Google Drive.

## Features:
- Downloads the highest quality video and audio available (up to 1080p).
- Uploads the downloaded video to a specified Google Drive folder.
- Automatically creates a folder named `ytvideo` in your Google Drive for storing videos.

## Prerequisites:
1. Python 3.x
2. Google Cloud project with Drive API enabled.
3. OAuth 2.0 credentials JSON file for Google Drive (Download from [Google Developer Console](https://console.cloud.google.com/)).

## Required Libraries:
Install the required libraries using:
```bash
pip install yt-dlp google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client requests
