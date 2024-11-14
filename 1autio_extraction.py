from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path, audio_output_path):
    # Load the video file
    video = VideoFileClip(f"{video_path}")
    
    # Extract audio from the video
    audio = video.audio
    
    # Write the audio to a file (e.g., MP3 or WAV)
    audio.write_audiofile(f"{audio_output_path}")

# Example usage
video_path = r"C:\Users\24adi\OneDrive\Desktop\intern\AI system Internship\AI-System\vids\Travis Scott - FE!N ft. Playboi Carti.mp4"

audio_output_path = r"C:\Users\24adi\OneDrive\Desktop\intern\AI system Internship\AI-System\audios\extracted_audio.mp3"

extract_audio_from_video(video_path, audio_output_path)
