import requests
import json
from _getting_aud_path import get_aud_path
from _script_generator import generate_costum_dis


if __name__ == "__main__":
    aud_paths = get_aud_path()

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
                return (transcribed_text)
            else:
                print(f"Error: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error during transcription: {e}")
            return None

    discriptions = []

    for aud_path in aud_paths:
        print("🔴🔴🔴🔴🔴🔴")
        text = transcribe_audio_to_text(aud_path)
        print (text)
        discriptions.append(text)


    strr = ' '.join(discriptions)

    print("🟡🟡🟡🟡🟡🟡🟡🟡🟡")
    print(strr)
    print("🟡🟡🟡🟡🟡🟡🟡🟡🟡")

    promptt = "Mimic the conversational, insightful, and thought-provoking style of a tech entrepreneur in an informal interview setting. Now, describe the impact of AI on various industries, focusing on its current influence, challenges, and its future potential. Dive deep into how AI is changing human-computer interaction, what hurdles it still faces, and what it means for countries like India in the AI race. Highlight examples and draw parallels to existing trends. Make the response engaging, as if explaining to a young tech enthusiast passionate about the future of AI.."
    
    res = generate_costum_dis(strr,promptt)

    print("🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵")
    print(f"{res}")
    print("🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵")

