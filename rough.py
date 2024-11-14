import instaloader
import os
import shutil

class InstagramScraper:
    def __init__(self, download_path):
        # Initialize Instaloader with video download enabled
        self.loader = instaloader.Instaloader(download_videos=True)
        self.download_path = download_path
        os.makedirs(self.download_path, exist_ok=True)

    def authenticate(self, username, password):
        """Authenticate using Instagram credentials."""
        self.loader.login(username, password)

    def fetch_creator_content(self, username, max_posts=5):
        """Fetch and download the first 'max_posts' reels of a specified user."""
        profile = instaloader.Profile.from_username(self.loader.context, username)
        posts = profile.get_posts()  # Fetching posts (reels are also included as video posts)

        count = 0
        for post in posts:
            if count >= max_posts:
                break
            if post.is_video:
                self.process_video(post)
                count += 1

    def process_video(self, post):
        """Download the specified video post to the target directory."""
        # Temporarily download the post to a subdirectory based on the shortcode
        temp_dir = f"temp_{post.shortcode}"
        self.loader.download_post(post, target=temp_dir)

        # Move downloaded files to the target download path
        for filename in os.listdir(temp_dir):
            src = os.path.join(temp_dir, filename)
            dest = os.path.join(self.download_path, filename)
            shutil.move(src, dest)
        
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)

# Usage
insta_scraper = InstagramScraper(download_path=r"C:\Users\24adi\OneDrive\Desktop\intern\AI system Internship\AI-System\vids\reels")
insta_scraper.authenticate("batburg1", "Upsidedown1234")
insta_scraper.fetch_creator_content("mrbeast", max_posts=5)
