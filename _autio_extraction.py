from moviepy.editor import VideoFileClip
from _getting_vid_path import get_vid_path

def extract_audio_from_video(video_path, audio_output_path):
    # Load the video file
    video = VideoFileClip(fr"{video_path}")
    
    # Extract audio from the video
    audio = video.audio
    
    # Write the audio to a file (e.g., MP3 or WAV)
    audio.write_audiofile(fr"{audio_output_path}")

# Example usage
def get_audio():
    video_paths = []
    video_paths = get_vid_path()

    i = 0
    for video_path in video_paths:
        i = i+1
        audio_output_path = fr"C:\Users\24adi\OneDrive\Desktop\intern\AI system Internship\AI-System\audios\extracted{i}.mp3"
        extract_audio_from_video(video_path,audio_output_path)

get_audio()