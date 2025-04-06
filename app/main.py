from reddit_scraper import fetch_reddit_video
from youtube_uploader import authenticate_youtube, upload_video

def main():
    print("📥 Fetching videos from Reddit...")
    title, video_path = fetch_reddit_video()
    print(f"🎬 Using original Reddit video: {title}")

    print("🔐 Authenticating YouTube...")
    youtube = authenticate_youtube()

    upload_video(
        youtube,
        file_path=video_path,
        title=title,
        description="Uploaded by Reddit Shorts Bot",
    )

if __name__ == "__main__":
    main()
