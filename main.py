import yt_dlp
import os
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
import requests

SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Function to authenticate Google Drive
def authenticate_google_drive():
    flow = InstalledAppFlow.from_client_secrets_file('path_to_your_client_secrets.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return build('drive', 'v3', credentials=creds)

# Upload file to Google Drive
def upload_to_drive(service, file_path, folder_id=None):
    file_metadata = {'name': os.path.basename(file_path)}
    if folder_id:
        file_metadata['parents'] = [folder_id]
    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file.get('id')

# Check internet connection
def check_internet_connection():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Wait for internet connection
def wait_for_internet(max_wait_time=600):
    start_time = time.time()
    while True:
        if check_internet_connection():
            return True
        elif time.time() - start_time > max_wait_time:
            print("You've been offline too long. Process canceled.")
            return False
        time.sleep(5)

# Download video using yt-dlp and upload to Google Drive
def download_video(url, service, folder_id):
    try:
        temp_dir = "temp_download"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        output_file = os.path.join(temp_dir, "downloaded_video.mp4")

        ydl_opts = {
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            'outtmpl': output_file,
            'merge_output_format': 'mp4'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from {url}...")
            ydl.download([url])
            print(f"Download completed! Saved as {output_file}")

        if not wait_for_internet():
            return None

        file_id = upload_to_drive(service, output_file, folder_id)
        print(f"Uploaded to Google Drive with file ID: {file_id}")

        os.remove(output_file)
        return file_id
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Main function
def main():
    service = authenticate_google_drive()
    ytvideo_folder_id = get_or_create_folder(service, "ytvideo")

    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url, service, ytvideo_folder_id)

# Helper function to create a folder in Google Drive
def get_or_create_folder(service, folder_name, parent_id=None):
    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'"
    if parent_id:
        query += f" and '{parent_id}' in parents"
    results = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    folders = results.get('files', [])
    if folders:
        return folders[0]['id']
    else:
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_id:
            folder_metadata['parents'] = [parent_id]
        folder = service.files().create(body=folder_metadata, fields='id').execute()
        return folder.get('id')

if __name__ == "__main__":
    main()
