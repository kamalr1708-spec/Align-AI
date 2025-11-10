# 🧠 Align-AI (ResumeTailor)

AI-powered web app that helps job seekers tailor resumes to job descriptions — improving ATS keyword match and generating custom summaries.

## 🚀 Features
- Ranks resume bullets using **TF-IDF** + **cosine similarity**
- Calculates **ATS keyword overlap**
- Generates tailored summaries via **Groq LLM** or offline fallback
- Built with **Streamlit** · Deployable on **Streamlit Cloud**

## 🧩 Tech Stack
Python · Streamlit · Scikit-learn · NumPy · Groq API · python-dotenv

## ⚙️ How It Works
1. Paste resume bullets and job description  
2. App ranks top-matching lines (TF-IDF + cosine)  
3. Computes ATS score  
4. Generates summary & bullet points (LLM or rule-based)

