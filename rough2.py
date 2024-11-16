import requests
import base64
from io import BytesIO
from pydub import AudioSegment  # For handling audio files

# Step 1: Define the function to encode audio into base64
def encode_audio(audio_path):
    try:
        with open(audio_path, 'rb') as audio_file:
            encoded_str = base64.b64encode(audio_file.read()).decode('utf-8')
        return encoded_str
    except FileNotFoundError:
        print(f"Error: The file {audio_path} was not found.")
        return None
    except Exception as e:
        print(f"Error encoding the audio: {e}")
        return None

# Step 2: Define the function to encode the text file into base64
def encode_text(text_path):
    try:
        with open(text_path, 'r') as text_file:
            text_content = text_file.read()
        # Optional: If the API expects the text to be base64-encoded, uncomment the next line
        # encoded_text = base64.b64encode(text_content.encode('utf-8')).decode('utf-8')
        return text_content  # or encoded_text if base64 is required
    except FileNotFoundError:
        print(f"Error: The file {text_path} was not found.")
        return None
    except Exception as e:
        print(f"Error encoding the text: {e}")
        return None

# Step 3: Define the function to send the encoded audio and text to the Hugging Face space
def get_cloned_audio(encoded_audio, text_content):
    try:
        API_URL = "https://de5282c3ca0c.7840f36b.ap-south-2.token.awswaf.com/de5282c3ca0c/526cf06acb0d/inputs?client=browser"  # Replace with the actual API endpoint you copied from the network tab
        response = requests.post(
            API_URL, 
            json={
                "data": [
                    f"data:audio/wav;base64,{encoded_audio}",
                    text_content  # Send the text content as is (or base64 if required by the API)
                ]
            }
        )
        
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        
        # Check if the response contains valid data
        if response.ok and 'data' in response.json():
            return response.json().get("data", [])[0][22:]  # Assuming response follows the same format as in the tutorial
        else:
            print(f"Error: Unexpected response format or empty data from the API.")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error sending request to the API: {e}")
        return None
    except Exception as e:
        print(f"Error in processing the API response: {e}")
        return None

# Step 4: Define the function to decode the base64 audio data and save it as a file
def decode_audio(base64_audio, output_path):
    try:
        audio_data = base64.b64decode(base64_audio)
        
        # Use BytesIO to simulate a file object
        audio = AudioSegment.from_wav(BytesIO(audio_data))
        
        # Save the decoded audio
        audio.export(output_path, format="wav")
        print(f"Audio saved to {output_path}")
        
    except Exception as e:
        print(f"Error decoding or saving audio: {e}")

# Main function to run the process
def clone_audio(input_audio, input_text, output_audio):
    # Encode the input audio file
    encoded_audio = encode_audio(input_audio)
    if not encoded_audio:
        return
    
    # Encode the input text file
    text_content = encode_text(input_text)
    if not text_content:
        return
    
    # Send the encoded audio and text content to the Hugging Face model and get the response
    cloned_audio_base64 = get_cloned_audio(encoded_audio, text_content)
    if not cloned_audio_base64:
        return
    
    # Decode the base64 audio response and save it
    decode_audio(cloned_audio_base64, output_audio)

# Example usage
input_text = r"C:\Users\24adi\OneDrive\Desktop\intern\AI system Internship\AI-System\use_this_ni.txt"  
# Path to your input text file

input_audio = r"C:\Users\24adi\OneDrive\Desktop\intern\AI system Internship\AI-System\use_this_nig.wav"
# Path to your input audio
output_audio = r"C:\Users\24adi\OneDrive\Desktop\intern\AI system Internship\AI-System\cloned_audio.wav"  # Path where the output audio will be saved

clone_audio(input_audio, output_audio)
