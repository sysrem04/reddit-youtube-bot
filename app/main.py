from app.reddit_scraper import fetch_reddit_video
from app.youtube_uploader import authenticate_youtube, upload_video
from app.music_adder import add_background_music

def main():
    print("📥 Fetching videos from Reddit...")
    title, video_path = fetch_reddit_video()

    print(f"🎬 Using original Reddit video: {title}")
    final_video_path = add_background_music(video_path)

    print("🔐 Authenticating YouTube...")
    youtube = authenticate_youtube()

    print("📤 Uploading...")
    upload_video(youtube, final_video_path, title, title)

if __name__ == "__main__":
    main()

