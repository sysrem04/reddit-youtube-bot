import os
import google.auth.transport.requests
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

def authenticate_youtube():
    print("🔐 Authenticating YouTube...")

    creds = Credentials.from_authorized_user_info({
        "client_id": os.getenv("YT_CLIENT_ID"),
        "client_secret": os.getenv("YT_CLIENT_SECRET"),
        "refresh_token": os.getenv("YT_REFRESH_TOKEN"),
        "token_uri": "https://oauth2.googleapis.com/token"
    })

    request = google.auth.transport.requests.Request()
    creds.refresh(request)

    return build("youtube", "v3", credentials=creds)

def upload_video(youtube, title, video_path):
    print("🚀 Uploading video to YouTube...")

    request_body = {
        "snippet": {
            "title": title,
            "description": "Reposted from Reddit r/kactress",
            "tags": ["shorts", "reddit", "kactress"],
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False,
        }
    }

    media_file = MediaFileUpload(video_path, mimetype="video/mp4", resumable=True)

    response = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media_file
    ).execute()

    print(f"✅ Upload successful! Video ID: {response['id']}")
