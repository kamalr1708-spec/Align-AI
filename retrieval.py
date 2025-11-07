import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def split_resume_lines(text):
    raw = re.split(r'\r?\n|•|\u2022|- ', text)
    return [ln.strip() for ln in raw if len(ln.strip()) > 20]

def compute_similarity(resume_lines, job_text):
    corpus = resume_lines + [job_text]
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2))
    tfidf = vectorizer.fit_transform(corpus)
    sims = cosine_similarity(tfidf[:-1], tfidf[-1]).reshape(-1)
    return sims

def ats_score(resume, job):
    words_r = set(re.findall(r"[a-zA-Z]+", resume.lower()))
    words_j = set(re.findall(r"[a-zA-Z]+", job.lower()))
    overlap = words_r & words_j
    return (round(len(overlap)/len(words_j)*100, 2) if words_j else 0), sorted(list(overlap))
