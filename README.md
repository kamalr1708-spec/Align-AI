🧠 Align-AI (ResumeTailor)

An AI-powered resume tailoring web app that helps job seekers align their resumes with specific job descriptions — improving ATS scores and making applications stand out.

🚀 Features

✍️ Resume Line Matching – Ranks resume bullets against job descriptions using TF-IDF and cosine similarity.

🤖 AI Summary Generation – Uses Groq LLM (Llama 3.1) to generate a professional tailored summary and bullet points.

⚙️ Offline Fallback – Works without an API key using a rule-based generator.

📊 ATS Keyword Score – Calculates keyword overlap between your resume and the job description.

🌐 Web App Interface – Built with Streamlit for an interactive, user-friendly experience.

🔐 Secure Key Management – Uses .env locally or Streamlit Secrets for deployment.

🧩 Tech Stack
Layer	Technology	Purpose
Frontend/UI	Streamlit	Build interactive interface for text input & results display
Core Logic	Python	Main programming language
Retrieval Engine	Scikit-learn (TF-IDF + cosine similarity)	Match resume lines to job descriptions
AI Integration	Groq API (LLM)	Generate tailored summary and refined bullets
Fallback Engine	Custom Rule-Based Generator	Works offline without API key
Environment Management	python-dotenv, Streamlit Secrets	Handle keys and config
Deployment	Streamlit Cloud	Easy hosting via GitHub integration
🧠 How It Works

Input:

Paste your resume bullets (one per line).

Paste a target job description.

Retrieve & Rank:

App splits resume into lines and compares each with the job using TF-IDF and cosine similarity.

Displays top-matching lines.

Score:

Calculates ATS keyword overlap %.

Generate:

If Groq key is available → calls Groq LLM (e.g., llama-3.1-8b-instant).

Otherwise → uses a local rule-based generator to compose summary + bullets.

Output:

Displays top matches, ATS score, and tailored summary/bullets.

Optionally allows PDF or text export.

🧰 Installation & Setup
🔧 Prerequisites

Python 3.10+

(Optional) Groq API Key

uv
 or pip for dependency management

🪜 Steps
# 1. Clone the repository
git clone https://github.com/yourusername/align-ai.git
cd align-ai

# 2. Install dependencies
uv add streamlit scikit-learn numpy python-dotenv groq
# or
pip install -r requirements.txt

# 3. Add your Groq key (optional)
echo "GROQ_API_KEY=your_key_here" > .env

# 4. Run the app
uv run streamlit run app.py
# or
streamlit run app.py


Then open your browser to 👉 http://localhost:8501

☁️ Deployment (Streamlit Cloud)

Push the project to your GitHub repo.

Go to share.streamlit.io
 → “New App.”

Select your repo → main branch → app.py.

Add your Groq API key under Settings → Secrets:

GROQ_API_KEY="gsk_..."


Click Deploy and enjoy your live app! 🎉

📂 Project Structure
E:\Rag
├── app.py             # Streamlit UI + main control flow
├── retrieval.py       # TF-IDF, cosine similarity, ATS overlap
├── generator.py       # rule_based_generator + Groq response parser
├── groq_client.py     # Safe wrapper around Groq API
├── utils.py           # Env loader, secret management
├── requirements.txt   # Dependencies
├── .gitignore         # Ignore .env, __pycache__, etc.
└── README.md          # Project documentation

📈 Example Workflow

Input:
✅ Resume Lines:

- Managed a 5-member team developing Python automation tools.  
- Implemented NLP models to analyze customer feedback.  


✅ Job Description:

Looking for a Python developer with experience in NLP, automation, and team leadership.


Output:

Top Matching Lines: NLP, automation, leadership

ATS Score: 72%

Tailored Summary:

Experienced Python developer with a strong background in NLP and automation, demonstrating leadership in managing high-performing teams.

Tailored Bullets:

Developed NLP-based customer insight models.

Automated business workflows with Python scripts.

Led a 5-member engineering team to successful project delivery.

🔐 Security Notes

Never commit .env or API keys to GitHub.

.gitignore includes .env by default.

Streamlit Secrets are encrypted and only accessible to your app at runtime.

🧭 Future Improvements

Replace TF-IDF with semantic embeddings for more accurate matching.

Add cover letter generation option.

Highlight keyword matches directly in the UI.

Enable PDF/Word export of the tailored resume.

✨ Author

[Your Name]
💼 Aspiring Data/AI Engineer
📧 your.email@example.com

🌐 LinkedIn Profile
 | GitHub
