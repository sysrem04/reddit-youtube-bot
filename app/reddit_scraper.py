import praw
import requests
import os
import uuid

def fetch_reddit_video():
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

    )

    subreddit = reddit.subreddit("kactress")
    for post in subreddit.hot(limit=10):
        if post.is_video and not post.stickied:
            video_url = post.media["reddit_video"]["fallback_url"]
            filename = f"downloads/{uuid.uuid4()}.mp4"
            os.makedirs("downloads", exist_ok=True)

            with requests.get(video_url, stream=True) as r:
                with open(filename, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

            return post.title, filename

    return "No valid video found", "downloads/sample.mp4"
