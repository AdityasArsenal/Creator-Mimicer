import requests
import json
from _getting_aud_path import get_aud_path

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3-turbo"

headers = {
    "Authorization": "Bearer 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"
}

def transcribe_audio_to_text(audio_file_path):
    try:
        with open(audio_file_path, 'rb') as audio_file:
            response = requests.post(API_URL, headers=headers, files={"file": audio_file})

        if response.status_code == 200:
            res = response.json()
            transcribed_text = res.get('text', '')
            print (transcribed_text)
            return (transcribed_text)
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

aud_paths = get_aud_path()

discriptions = []
for aud_path in aud_paths:
    print("🔴🔴🔴🔴🔴🔴")
    text = transcribe_audio_to_text(aud_path)
    discriptions.append(text)

res = ' '.join(discriptions)

print("🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡")
print(f"{res}")
print("🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡")
