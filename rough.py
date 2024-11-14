import instaloader
from moviepy.editor import VideoFileClip
import os
import logging
import shutil

class InstagramScraper:
    def __init__(self):
        self.loader = instaloader.Instaloader(download_videos=True)
        self.temp_dir = "temp_downloads"
        os.makedirs(self.temp_dir, exist_ok=True) 

    def authenticate(self, username: str, password: str) -> bool:
        """Authenticate the user using provided Instagram credentials."""
        try:
            self.loader.login(username, password)
            return True
        except Exception as e:
            logging.error(f"Authentication failed: {e}")
            return False

    def fetch_creator_content(self, username: str, max_posts: int = 10):
        """Fetch content from a given Instagram creator's profile."""
        try:
            profile = instaloader.Profile.from_username(self.loader.context, username)
            posts = profile.get_posts()
            videos, captions = [], []

            for post in posts:
                if len(videos) >= max_posts:
                    break
                if post.is_video:
                    video_data = self._process_video(post)
                    if video_data:
                        videos.append(video_data)
                        captions.append(post.caption or "")
            
            self._cleanup_temp_files()  # Cleanup temporary files after fetching content
            return {'videos': videos, 'captions': captions}
        except Exception as e:
            logging.error(f"Content fetching failed: {e}")
            return None

    def _process_video(self, post):
        """Process the video by downloading and extracting audio."""
        try:
            video_path = f"{self.temp_dir}/{post.shortcode}.mp4"
            self.loader.download_post(post, target=self.temp_dir)

            with VideoFileClip(video_path) as video:
                audio_path = self._extract_audio(video, post.shortcode)
                return {
                    'duration': video.duration,
                  
                    'audio_path': audio_path
                }
        except Exception as e:
            logging.error(f"Video processing failed for {post.shortcode}: {e}")
            return None

    def _extract_audio(self, video, shortcode):
        """Extract audio from the video and save it as an MP3 file."""
        audio_path = f"{self.temp_dir}/audio_{shortcode}.mp3"
        try:
            video.audio.write_audiofile(audio_path)
            return audio_path
        except Exception as e:
            logging.error(f"Audio extraction failed for {shortcode}: {e}")
            return None

    def _cleanup_temp_files(self):
        """Remove temporary files to avoid using up disk space."""
        try:
            shutil.rmtree(self.temp_dir)
            logging.info(f"Temporary files cleaned up from {self.temp_dir}.")
        except Exception as e:
            logging.error(f"Failed to clean up temporary files: {e}")

insta = InstagramScraper

insta.authenticate()