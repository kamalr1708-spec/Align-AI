# groq_client.py
# Clean version – safe even if Groq is not installed

import os

def groq_available() -> bool:
    """Return True if the groq package is importable."""
    try:
        import groq  # local import so import errors don’t break module
        return True
    except Exception:
        return False


def generate_with_groq(job_text, retrieved_lines, model="llama3-8b-8192"):
    """
    Minimal placeholder that calls Groq if available.
    If groq is not installed or the API key is missing, raises a RuntimeError.
    """
    try:
        from groq import Groq
    except Exception as e:
        raise RuntimeError("groq package not installed. Run: uv add groq") from e

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set. Put it in your .env file.")

    client = Groq(api_key=api_key)
    prompt = (
        "You are ResumeTailor, a tool that rewrites resumes for specific jobs.\n"
        "Job Description:\n" + job_text + "\n\n"
        "Relevant Resume Lines:\n" + "\n".join(retrieved_lines) + "\n\n"
        "Return sections:\nSUMMARY:\n<2–3 sentences>\n\nBULLETS:\n- bullet 1\n- bullet 2\n- bullet 3"
    )

    result = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=400
    )
    return result.choices[0].message.content.strip()
