import os

def get_vid_path():

    initial_directory = r'C:\Users\24adi\OneDrive\Desktop\intern\AI system Internship\AI-System\vids\reels'
    
    files_names = os.listdir(initial_directory)
    file_paths = []

    for file_name in files_names:
        if file_name.endswith(".mp4"):
            file_path = os.path.join(initial_directory,file_name)
            file_paths.append(file_path)

    return file_paths
