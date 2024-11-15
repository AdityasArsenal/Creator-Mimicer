import instaloader
import os
import shutil

loader = instaloader.Instaloader()

class instagramm:
    def __init__(self,path):
        self.loader = instaloader.Instaloader(download_videos=True)
        self.downlode_path=path
        os.makedirs(self.downlode_path,exist_ok=True)
        

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
            
    def process_video(self,reel):
        video_tmp_dir = f"temp_{reel.shortcode}"
        self.loader.download_post(reel, target=video_tmp_dir)

        for filename in os.listdir(video_tmp_dir):
            scr = os.path.join(video_tmp_dir,filename)
            destination = os.path.join(self.downlode_path,filename)
            shutil.move(scr,destination)
        
def insta_lod(username):

    insta = instagramm(path=r"C:\Users\24adi\OneDrive\Desktop\intern\AI system Internship\AI-System\vids\reels")
    insta.authenticate("fire_film5","Upsidedown123")
    insta.fetch_creator_content(f"{username}",16)

insta_lod("thevarunmayya")
