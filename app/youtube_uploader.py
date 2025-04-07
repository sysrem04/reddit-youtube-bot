import os
import json
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

def authenticate_youtube():
    client_id = os.environ['YOUTUBE_CLIENT_ID']
    client_secret = os.environ['YOUTUBE_CLIENT_SECRET']
    refresh_token = os.environ['YOUTUBE_REFRESH_TOKEN']

    creds_data = {
        "token": None,
        "refresh_token": refresh_token,
        "token_uri": "https://oauth2.googleapis.com/token",
        "client_id": client_id,
        "client_secret": client_secret,
        "scopes": ["https://www.googleapis.com/auth/youtube.upload"]
    }

    creds = Credentials.from_authorized_user_info(info=creds_data)
    
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    
    youtube = build('youtube', 'v3', credentials=creds)
    return youtube
