# YouTube Video Downloader and Google Drive Uploader

This Python script allows you to download a YouTube video and automatically upload it to your Google Drive.

## Features
- Downloads the highest quality video and audio available (up to 1080p).
- Uploads the downloaded video to a specified folder in your Google Drive.
- Automatically creates a folder named `ytvideo` in your Google Drive for storing videos.

## Prerequisites
Before running the script, ensure you have the following:

1. **Python 3.x**: Install from [python.org](https://www.python.org/downloads/).
2. **Google Cloud Project**: You need to create a Google Cloud project with the Drive API enabled.
3. **OAuth 2.0 Credentials**: Download the OAuth 2.0 credentials JSON file for your project from the [Google Developer Console](https://console.cloud.google.com/).

## Required Libraries
You will need to install the following libraries. Use the command below to install them via pip:

```bash
pip install yt-dlp google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client requests
```

## Setup Instructions
Follow these steps to set up and run the script:

1. **Clone the Repository**:
   Open your terminal or command prompt and clone the repository:
   ```bash
   git clone https://github.com/Clay990/ytvideo.git
   cd ytvideo
   ```

2. **Move Credentials File**:
   Place your `client_secrets.json` file (the downloaded OAuth 2.0 credentials) into the project directory. You can rename it if needed but make sure to update the path in the script where it says `path_to_your_client_secrets.json`.

3. **Run the Script**:
   Execute the script using Python. Open your terminal or command prompt and run:
   ```bash
   python main.py
   ```

4. **Authenticate with Google Drive**:
   The first time you run the script, it will open a web browser window asking you to authenticate with your Google account and allow access to Google Drive. Follow the on-screen instructions.

5. **Enter YouTube Video URL**:
   After authentication, the script will prompt you to enter the YouTube video URL you wish to download. Paste the URL and press Enter.

6. **Check Google Drive**:
   Once the download is complete, the video will be uploaded to the `ytvideo` folder in your Google Drive. You can verify the upload by checking your Drive.

## Notes
- Ensure you have a stable internet connection while running the script, as it requires downloading the video and uploading it to Google Drive.
- If you encounter any errors, make sure that all libraries are installed correctly and that your OAuth 2.0 credentials are properly set up.

## License
