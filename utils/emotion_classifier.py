# utils/emotion_classifier.py
import os
from dotenv import load_dotenv
from mistralai import Mistral
load_dotenv()
api_key=os.getenv("MISTRAL_API_KEY")
base_url="https://api.mistral.ai/v1"

client = Mistral(api_key=api_key)

def detect_emotion(text: str) -> str:
    prompt = (
        "Voici un rêve :\n"
        f"{text}\n\n"
        "Analyse et dis-moi s’il est : heureux, stressant ou neutre. "
        "Réponds uniquement par l’un de ces mots."
    )

    try:
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[{"role": "system", "content": "Tu es un détecteur d'émotions de rêves."}, 
                      {"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip().lower()
    except Exception as e:
        return f"Erreur API : {e}"
