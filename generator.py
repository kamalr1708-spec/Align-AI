# generator.py
import re

def rule_based_generator(job_text, retrieved_lines):
    """Simple fallback generator for ResumeTailor."""
    words = re.findall(r"[a-zA-Z]{3,}", job_text.lower())
    top = sorted(set(words), key=lambda x: words.count(x), reverse=True)[:5]
    summary = f"Experienced professional with skills in {', '.join(top)}."
    summary += " " + " ".join(retrieved_lines[:2])
    bullets = [ln.strip() for ln in retrieved_lines[:3]] or ["Relevant experience available."]
    return summary, bullets

def parse_groq_output(raw_text):
    """Parse Groq response into summary + bullet list."""
    parts = re.split(r"SUMMARY:|BULLETS:", raw_text, flags=re.IGNORECASE)
    summary = parts[1].strip() if len(parts) > 1 else raw_text.split("\n")[0]
    bullets = []
    if len(parts) > 2:
        bullets = [b.strip("- \n") for b in parts[2].splitlines() if b.strip()]
    return summary, bullets
