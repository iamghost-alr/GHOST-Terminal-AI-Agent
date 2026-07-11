import os
import re
import subprocess

from config import APPS

# Filler words stripped out before matching an app name.
_FILLER = [
    "open", "launch", "start", "access",
    "application", "app", "the", "for", "me", "please", "and",
]

# Strips whole filler WORDS only, never substrings inside other words.
_FILLER_RE = re.compile(
    r"\b(?:" + "|".join(_FILLER) + r")\b",
    re.IGNORECASE,
)


def _clean(text):
    text = _FILLER_RE.sub(" ", text)
    text = re.sub(r"\s+", " ", text)
    return text.lower().strip()


def _open_one(app_name):
    """Try to launch a single app by config key.

    Returns a short status string.
    """
    path = APPS.get(app_name)

    if not path:
        return f"I don't have an app called '{app_name}' configured."

    if not os.path.exists(path):
        return f"Couldn't find '{app_name}' at the saved path: {path}"

    try:
        subprocess.Popen([path])
        return f"opened {app_name}"
    except Exception as e:
        return f"failed to open {app_name}: {e}"


def open_app(query):
    """Launch one or more desktop apps by name.

    Understands "open brave and calculator" -> launches both.
    """

    cleaned = _clean(query)

    # Find every configured app name that appears in the query.
    matched = [name for name in APPS if name in cleaned]

    if not matched:
        available = ", ".join(APPS)
        return f"Application not found. I can open: {available}."

    results = [_open_one(name) for name in matched]

    if len(results) == 1:
        return results[0].capitalize() + "."

    # Multiple: join into one readable line.
    return "Done — " + ", ".join(results) + "."
