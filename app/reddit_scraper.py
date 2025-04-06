import os
import praw
import requests
import random

def fetch_reddit_video(subreddit_name="kactress"):
    print("📥 Fetching videos from Reddit...")

    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    subreddit = reddit.subreddit(subreddit_name)
    posts = list(subreddit.hot(limit=20))

    video_posts = [post for post in posts if hasattr(post, "media") and post.media]

    if not video_posts:
        raise Exception("❌ No video posts found.")

    post = random.choice(video_posts)
    title = post.title
    video_url = post.media["reddit_video"]["fallback_url"]

    video_path = "video.mp4"
    with open(video_path, "wb") as f:
        f.write(requests.get(video_url).content)

    print(f"🎬 Using original Reddit video: {title}")
    return title, video_path
