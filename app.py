import os
import numpy as np
import streamlit as st
from retrieval import split_resume_lines, compute_similarity, ats_score
from generator import rule_based_generator, parse_groq_output
from groq_client import groq_available, generate_with_groq
from utils import ensure_env_loaded

ensure_env_loaded()

st.set_page_config(page_title="Aligh-AI", page_icon="", layout="centered")
st.title("AlignAI-Resume Optimization Assistant")

# Inputs
with st.expander("PASTE - Resume ", expanded=True):
    resume_text = st.text_area("Resume text", height=220,
        placeholder="Paste your resume here  (one bullet per line)...")

with st.expander("PASTE - Job Description", expanded=True):
    job_text = st.text_area("Job description text", height=200, placeholder="Paste job description here...")

col1, col2, col3 = st.columns([1,1,1])
with col1:
    top_k = st.number_input("Top-K lines", min_value=1, max_value=20, value=5)
with col2:
    model_choice = st.selectbox("Groq model", ["llama-3.1-8b-instant", "llama-3.3-70b-versatile"])
with col3:
    run_btn = st.button("Generate Optimized Summary")

if run_btn:
    if not resume_text or not job_text:
        st.warning("Please paste both resume and job description.")
    else:
        lines = split_resume_lines(resume_text)
        if not lines:
            st.error("No valid resume lines found.")
        else:
            st.info("Computing TF-IDF similarities locally...")
            sims = compute_similarity(lines, job_text)
            k = min(int(top_k), len(lines))
            ranked_idx = np.argsort(sims)[::-1][:k]
            retrieved = [lines[i] for i in ranked_idx]

            st.subheader("TOP Matching Lines")
            for i, idx in enumerate(ranked_idx, start=1):
                st.markdown(f"**{i}.** (score={sims[idx]:.3f}) — {lines[idx]}")

            score, overlaps = ats_score(resume_text, job_text)
            st.metric("[--ATS Keyword Overlap--]", f"{score}%")
            if overlaps:
                st.write("Sample overlaps:", ", ".join(overlaps[:30]))

            groq_key = os.getenv("GROQ_API_KEY")
            if groq_key and groq_available():
                st.info("Generating with Groq...")
                try:
                    raw = generate_with_groq(job_text, retrieved, model=model_choice)
                    st.text_area("Groq Raw Output", value=raw, height=220)
                    summary, bullets = parse_groq_output(raw)
                    st.subheader("Optimized Summary")
                    st.write(summary)
                    st.subheader("Bullets")
                    for b in bullets[:3]:
                        st.write(f"- {b}")
                except Exception as e:
                    st.error(f"Groq failed: {e}")
                    summary, bullets = rule_based_generator(job_text, retrieved)
                    st.write(summary)
                    for b in bullets:
                        st.write(b)
            else:
                st.warning("No Groq key found — using local rule-based generator.")
                summary, bullets = rule_based_generator(job_text, retrieved)
                st.write(summary)
                for b in bullets:
                    st.write(b)

st.divider()
st.caption("Powered By ALIGN-AI")
