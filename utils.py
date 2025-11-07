# utils.py
"""
Utility helpers for ResumeTailor

Functions:
- ensure_env_loaded(): loads .env if python-dotenv is available
- read_groq_key_file(): read Groq key from groq.key
- read_config_json(): read configuration from config.json
- get_groq_key(): find and return GROQ_API_KEY from env, .env, groq.key, or config.json
- set_groq_key_env(): manually set GROQ_API_KEY in this runtime
"""

import os
import json


def ensure_env_loaded():
    """Try to load .env using python-dotenv if installed."""
    try:
        from dotenv import load_dotenv  # Lazy import so no hard dependency
        load_dotenv()
        return True
    except Exception:
        # If python-dotenv not installed, just skip
        return False


def read_groq_key_file(path: str = "groq.key") -> str | None:
    """Read Groq key from a simple text file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            key = f.read().strip()
            return key if key else None
    except FileNotFoundError:
        return None
    except Exception:
        return None


def read_config_json(path: str = "config.json") -> dict:
    """Read config.json (optional)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f) or {}
    except Exception:
        return {}


def get_groq_key() -> str | None:
    """
    Get the Groq API key with this priority:
    1. Environment variable GROQ_API_KEY
    2. .env file (if python-dotenv installed)
    3. groq.key file
    4. config.json
    """
    # 1. Environment variable
    key = os.getenv("GROQ_API_KEY")
    if key:
        return key

    # 2. .env file
    try:
        ensure_env_loaded()
        key = os.getenv("GROQ_API_KEY")
        if key:
            return key
    except Exception:
        pass

    # 3. groq.key file
    key = read_groq_key_file()
    if key:
        os.environ["GROQ_API_KEY"] = key
        return key

    # 4. config.json
    cfg = read_config_json()
    key = cfg.get("GROQ_API_KEY")
    if key:
        os.environ["GROQ_API_KEY"] = key
        return key

    return None


def set_groq_key_env(key: str) -> bool:
    """Set GROQ_API_KEY in this runtime (does not persist)."""
    if key:
        os.environ["GROQ_API_KEY"] = key
        return True
    return False
