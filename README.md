# 🌙 Synthétiseur de rêves

Transformez vos rêves en mots, en images et en émotions.  
Une application Web magique ✨ qui vous permet d’enregistrer vos rêves, de les transcrire, de les illustrer avec une IA, d’analyser leur ambiance émotionnelle… et de les conserver dans un journal personnel onirique.

---

## 📸 Aperçu

![Aperçu de l'application](assets/preview.jpg)

---

## 🚀 Fonctionnalités

✅ Enregistrement ou téléversement d’un rêve (audio)  
📝 Transcription vocale automatique (via Groq API + LLM)  
🎨 Génération d’image par IA (ClipDrop API)  
😴 Détection d’émotion du rêve (LLM Mistral)  
📚 Historique des rêves avec audio, texte, image  
🗑️ Suppression des rêves individuellement

---

## 🛠️ Tech Stack

- **Frontend** : [Streamlit](https://streamlit.io/) ≥ 1.35
- **Speech-to-text** : [Groq API + LLM](https://groq.com/)
- **Text-to-image** : [ClipDrop API (Stability AI)](https://clipdrop.co/apis)
- **Emotion classifier** : [Mistral API](https://console.mistral.ai/)
- **Python** : 3.12+

---

## 📋 1. Dossier de cadrage

### 🎨 1.1 Étude d’art / Benchmark des APIs

| API / Service             | Usage                         | Coût 💰        | Quota / Limite         | Temps de réponse ⏱️ | RGPD 🇪🇺 |
|---------------------------|-------------------------------|----------------|-------------------------|----------------------|---------|
| **Groq (LLM + audio)**    | Transcription + réponse rapide | Gratuit (pour dev) | 10 req/s (LLM Groq/Gemma) | ⚡ Ultra-rapide (<1s) | ✅ Oui  |
| **ClipDrop (Stability AI)** | Génération d’images (text-to-image) | Gratuit <br> (25-100/mois) | 1 image / req <br> Limite quotidienne | ⚡ 2-3 sec/image      | ⚠️ Stockage tiers |
| **Mistral API**           | Classification émotionnelle (LLM) | Gratuit (1000 req/mois) | 4000 tokens / min      | ⚡ 0.5 - 1 sec         | ✅ Oui  |
| **OpenAI (optionnel)**    | LLM alternatif (GPT)          | $ (payant)     | 3M tokens / mois (selon plan) | ⏱️ Très rapide        | ✅ Oui  |

📌 **Conclusion** : ce projet utilise principalement **Groq**, **Mistral**, et **ClipDrop**, tous accessibles gratuitement et compatibles avec une démarche RGPD dans un cadre éducatif.

---

### 🧠 1.2 Séquence clé – Traitement d’un rêve (UML fonctionnel)

```mermaid
graph TD

    Audio utilisateur --> Transcription Groq LLM --> Texte du rêve --> Image générée (ClipDrop) --> Analyse émotionnelle (Mistral) --> Affichage : audio + texte + image + émotion
```
 
---

## 📦 Installation

1. **Clone le projet** :

```bash
git clone https://github.com/morningstar-47/synthetiseur_reves.git
cd synthetiseur_reves
```

2. **Installe les dépendances** :

```bash
pip install -r requirements.txt
```

3. **Ajoute un fichier `.env` à la racine** :

```env
CLIPDROP_API_KEY=ta_cle_api_clipdrop
MISTRAL_API_KEY=ta_cle_api_mistral
GROQ_API_KEY=ta_cle_api_groq
```

4. **Lance l'application** :

```bash
streamlit run app.py
```

---

## 📁 Arborescence

```
synthetiseur-de-reves/
│
├── app.py
├── requirements.txt
├── .env
│
├── dreams/
│   ├── audios/
│   └── transcriptions/
│
├── assets/              # images générées
├── utils/
│   ├── speech_to_text.py
│   ├── generate_image.py
│   ├── emotion_classifier.py
│   └── dashboard.py
```

---

## ☁️ Déploiement (Streamlit Cloud)

1. Crée un repo GitHub
2. Pousse ton code
3. Va sur [https://streamlit.io/cloud](https://streamlit.io/cloud)
4. Lien vers ton repo → Configure `.env secrets` → Déploie 🚀

---

## ✨ À venir

- 🎤 Enregistrement vocal direct dans l'app
- 📊 Statistiques de rêve (mots-clés, humeur, nuages de mots)
- 🔒 Authentification utilisateur (multi-profils)
- 💾 Sauvegarde cloud / export PDF des rêves

---

## 🧙 Auteur

Développé avec amour par [Emmanuel](https://github.com/morningstar-47)  
Projet académique ✨ – librement inspiré de l’inconscient collectif 🌌

---

## 🪪 Licence

MIT License – libre à toi d’améliorer, transformer, ou rêver avec 💭