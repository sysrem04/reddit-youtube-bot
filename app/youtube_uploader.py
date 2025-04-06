import os
import pickle
import time
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate_youtube():
    creds = None
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(BASE_DIR, "creds", "token.pickle")
    creds_path = os.path.join(BASE_DIR, "creds", "client_secret.json")

    if os.path.exists(token_path):
        with open(token_path, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                creds_path, SCOPES)
            creds = flow.run_local_server(port=8080, open_browser=False)

        with open(token_path, "wb") as token:
            pickle.dump(creds, token)

    print("✅ YouTube authenticated successfully.")
    return build("youtube", "v3", credentials=creds)


def upload_video(youtube,
                 file_path,
                 title,
                 description,
                 tags=None,
                 categoryId="22",
                 privacyStatus="public"):
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags or [],
            "categoryId": categoryId
        },
        "status": {
            "privacyStatus": privacyStatus,
            "selfDeclaredMadeForKids": False
        }
    }

    media = MediaFileUpload(file_path, mimetype="video/mp4", resumable=True)

    print("🚀 Uploading to YouTube Shorts...")
    request = youtube.videos().insert(part="snippet,status",
                                      body=body,
                                      media_body=media)

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"📄 Upload progress: {int(status.progress() * 100)}%")
        time.sleep(1)

    print(f"✅ Upload successful! Video ID: {response['id']}")
    return response
