# utils/speech_to_text.py
import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def transcribe_audio(file_path: str, language: str = "fr"):
    try:
        # Ouvre le fichier audio
        with open(file_path, "rb") as file:
            # Crée une transcription du fichier audio
            transcription = client.audio.transcriptions.create(
                file=file,  # Fichier audio requis
                model="whisper-large-v3-turbo",  # Modèle requis pour la transcription
                prompt="Extrait le texte de l'audio de la maniere la plus précise  possible",  # Optionnel
                response_format="verbose_json",  # Optionnel
                timestamp_granularities=["word", "segment"],  # Optionnel
                language=language,  # Optionnel (français par défaut)
                temperature=0.0  # Optionnel
            )
            return transcription.text
    except Exception as e:
        return f"Erreur lors de la transcription : {e}"





