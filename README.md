🧠 Align-AI (ResumeTailor)

AI-powered web app that helps job seekers tailor resumes to job descriptions — improving ATS keyword match and generating custom summaries.

🚀 Features

🔍 Ranks resume bullets using TF-IDF and cosine similarity.

📊 Computes ATS keyword overlap score.

🤖 Generates tailored summaries via Groq LLM (or offline fallback).

🌐 Built with Streamlit — deployable on Streamlit Cloud.

🧩 Tech Stack

Python · Streamlit · Scikit-learn · NumPy · Groq API · python-dotenv

⚙️ How It Works

Paste resume bullets + job description.

App ranks most relevant lines (TF-IDF + cosine similarity).

Calculates ATS score.

Generates summary & tailored bullets (LLM or rule-based).

🪜 Run Locally
git clone https://github.com/yourusername/align-ai.git
cd align-ai
pip install -r requirements.txt
streamlit run app.py


Add your Groq API key in a .env file:

GROQ_API_KEY=your_key_here


Then open 👉 http://localhost:8501

☁️ Deployment

Deploy easily on Streamlit Cloud — connect your GitHub repo and add your API key in Secrets:

GROQ_API_KEY="gsk_..."

🧭 Future Ideas

Add semantic embeddings for smarter matching.

Include cover letter generation.

Highlight matched keywords in UI.

