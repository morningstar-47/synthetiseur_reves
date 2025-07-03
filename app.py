# app.py
import streamlit as st
from utils.speech_to_text import transcribe_audio
from utils.generate_image import generate_image
from utils.emotion_classifier import detect_emotion
from utils.dashboard import get_all_dreams
import os
from dotenv import load_dotenv

load_dotenv()

# 🌙 Configuration
st.set_page_config(
    page_title="🌙 Synthétiseur de rêves",
    page_icon="🌀",
    layout="centered"
)

st.markdown("""
    <h1 style='text-align: center; color: #5A00B0;'>🌌 Synthétiseur de rêves</h1>
    <p style='text-align: center; font-size: 18px; color: #666;'>Transformez vos rêves en images et émotions ✨</p>
    <hr style="border:1px solid #aaa">
""", unsafe_allow_html=True)

# 🎤 Étape 1 : Upload
st.markdown("### 🎙️ 1. Racontez votre rêve")
uploaded_file = st.file_uploader("Téléversez un fichier audio (.wav, .mp3, .m4a)", type=["wav", "mp3", "m4a"])

if uploaded_file:
    audio_path = f"dreams/audios/{uploaded_file.name}"
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("✅ Audio reçu avec succès !")

    # 📝 Étape 2 : Transcription
    st.markdown("### 📝 2. Transcription automatique du rêve")
    with st.spinner("🔄 Transcription en cours..."):
        transcription = transcribe_audio(audio_path)
        st.text_area("🗒️ Résultat :", transcription, height=200)

        # Enregistrement
        transcription_path = f'dreams/transcriptions/{uploaded_file.name}.txt'
        with open(transcription_path, 'w', encoding='utf-8') as f:
            f.write(transcription)

    # 🖼️ Étape 3 : Génération d’image
    st.markdown("### 🖼️ 3. Génération d’une image à partir du rêve")
    if st.button("✨ Créer une image onirique"):
        output_img = f"assets/{uploaded_file.name}.jpg"
        with st.spinner("🎨 Génération en cours..."):
            if generate_image(transcription, output_img):
                st.image(output_img, caption="🌠 Votre rêve illustré", use_container_width=True)
            else:
                st.error("❌ Impossible de générer une image.")

    # 😴 Étape 4 : Analyse émotionnelle
    st.markdown("### 😴 4. Analyse de l’émotion du rêve")
    with st.spinner("🧠 Analyse en cours..."):
        emotion = detect_emotion(transcription)
        if "erreur" in emotion.lower():
            st.error(emotion)
        else:
            st.success(f"💫 Émotion détectée : **{emotion.capitalize()}**")

# 📚 Historique des rêves
st.markdown("---")
st.markdown("### 📚 5. Historique de vos rêves")

dreams = get_all_dreams()
if not dreams:
    st.info("🕸️ Aucun rêve enregistré pour l’instant.")
else:
    for dream in dreams[::-1]:
        with st.expander(f"🎧 {dream['filename']}"):
            st.audio(dream['audio'])

            st.markdown("#### 📝 Transcription")
            st.write(dream['transcription'])

            st.markdown("#### 🖼️ Image générée")
            if dream["image"]:
                st.image(dream["image"], use_container_width=True)
            else:
                st.warning("⚠️ Aucune image générée pour ce rêve.")
