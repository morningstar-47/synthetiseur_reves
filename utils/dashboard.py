import os

def get_all_dreams():
    dreams = []
    audio_dir = "dreams/audios"
    transcription_dir = "dreams/transcriptions"
    image_dir = "assets"

    for file in os.listdir(audio_dir):
        if not file.lower().endswith((".mp3", ".wav", "m4a")):
            continue

        # On garde le nom complet avec extension pour correspondre aux autres fichiers
        audio_path = os.path.join(audio_dir, file)
        transcription_path = os.path.join(transcription_dir, f"{file}.txt")
        image_path = os.path.join(image_dir, f"{file}.jpg")

        # Lecture de la transcription si elle existe
        if os.path.exists(transcription_path):
            with open(transcription_path, "r", encoding="utf-8") as f:
                transcription = f.read()
        else:
            transcription = "[Transcription absente]"

        dream = {
            "filename": file,
            "audio": audio_path,
            "transcription": transcription,
            "image": image_path if os.path.exists(image_path) else None
        }
        dreams.append(dream)

    return dreams


def delete_dream(filename: str):
    base_audio = f"dreams/audios/{filename}"
    base_transcription = f"dreams/transcriptions/{filename}.txt"
    base_image = f"assets/{filename}.jpg"

    # Suppression sécurisée
    for path in [base_audio, base_transcription, base_image]:
        try:
            if os.path.exists(path):
                os.remove(path)
        except Exception as e:
            print(f"Erreur lors de la suppression de {path} : {e}")