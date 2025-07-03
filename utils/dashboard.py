# # utils/dashboard.py
# import os

# def get_all_dreams():
#     dreams = []
#     audio_files = os.listdir("dreams/audios")

#     # Boucle pour parcourir tous les fichiers de transcription
#     print("--- Parcours des transcriptions ---")
#     for transcription_file in os.listdir("dreams/transcriptions"):
#         print("transcription_path:", os.path.join("dreams/transcriptions", transcription_file))

#     # Boucle pour parcourir toutes les images
#     print("--- Parcours des images ---")
#     if os.path.exists("assets"):
#         for image_file in os.listdir("assets"):
#             print("image_path:", os.path.join("assets", image_file))

#     for audio_file in audio_files:
#         base_name = os.path.splitext(os.path.basename(audio_file))[0]
#         transcription_path = f"dreams/transcriptions/{base_name}.txt"
#         image_path = f"assets/{base_name}.jpg"
        
#         try:
#             with open(transcription_path, "r", encoding="utf-8") as f:
#                 transcription = f.read()
#         except Exception as e:
#             print(f"Erreur lors de l'ouverture du fichier {transcription_path} : {e}")
#             transcription = "[Transcription manquante]"

#         dream = {
#             "audio": audio_file,
#             "transcription": transcription,
#             "image": image_path if os.path.exists(image_file) else None
#         }
#         dreams.append(dream)
    
#     return dreams

# utils/dashboard.py
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
