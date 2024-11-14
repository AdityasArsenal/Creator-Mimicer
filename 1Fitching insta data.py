import instaloader
import os

loader = instaloader.Instaloader

class int:
    def __init__(self):
        self.loader = instaloader.Instaloader(download_videos=True)

    def authenticate(self,username, password):
        self.loader.login(username,password)

    def fetch_creator_content(self, username: str, max_posts):

        profile = instaloader.Profile.from_username(self.loader.context, username)
        reels = profile.get_reels()
        videos, captions = [], []

        c = 0
        for reel in reels:
            if c >= max_posts:
                break
            if reel.is_video:
                video_data = self.process_video(reel)
                c = c+1
                if video_data:
                    videos.append(video_data)
                    captions.append(reel.caption or "")
            
    def process_video(self,reel):
            self.video_path = r"C:\Users\24adi\OneDrive\Desktop\intern\AI system Internship\AI-System\vids"
            self.loader.download_post(reel, target=f"{self.video_path}")


insta = int()
insta.authenticate("batburg1","Upsidedown1234")
insta.fetch_creator_content("mrbeast",5)