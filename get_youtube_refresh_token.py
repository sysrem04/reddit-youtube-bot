from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def main():
    flow = InstalledAppFlow.from_client_config({
        "installed": {
            "client_id": "PASTE_CLIENT_ID",
            "client_secret": "PASTE_CLIENT_SECRET",
            "redirect_uris": ["http://localhost"],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token"
        }
    }, SCOPES)

    creds = flow.run_local_server(port=8080, open_browser=True)

    print("\n✅ Refresh token berhasil dibuat!")
    print("🔑 refresh_token:\n")
    print(creds.refresh_token)

if __name__ == "__main__":
    main()
