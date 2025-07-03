# utils/generate_image.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CLIPDROP_API_KEY")

def generate_image(prompt: str, output_path: str) -> bool:
    url = "https://clipdrop-api.co/text-to-image/v1"
    headers = {"x-api-key": API_KEY}
    data = {
        "prompt": (None, 'Tu es un artiste qui génère des images à partir de textes de rêves : ' + prompt, 'text/plain'),
    }

    response = requests.post(url, headers=headers, files=data)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        return True
    else:
        print("Erreur Clipdrop :", response.text)
        return False
