import re
import webbrowser
from urllib.parse import quote_plus

from config import SITES, SEARCH_URL

_FILLER = [
    "open", "launch", "go", "to", "visit", "browse",
    "the", "site", "website", "for", "me", "please", "and", "show",
]

# Matches a raw URL or a bare domain like "reddit.com/r/python".
_URL_RE = re.compile(
    r"\b(?:https?://)?(?:[a-z0-9-]+\.)+[a-z]{2,}(?:/[^\s]*)?\b",
    re.IGNORECASE,
)

# Strips whole filler WORDS only, never substrings inside other words
# (so "me" won't corrupt "mechanical", "to" won't corrupt "youtube").
_FILLER_RE = re.compile(
    r"\b(?:" + "|".join(_FILLER) + r")\b",
    re.IGNORECASE,
)


def _clean(text):
    text = _FILLER_RE.sub(" ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def open_sites(query):
    """Full browser control.

    Priority:
      1. Known site name (from config.SITES) -> open its URL.
      2. Raw URL / bare domain in the query  -> open it directly.
      3. Anything else                        -> open a browser search.
    """

    cleaned = _clean(query)

    # 1. Known site?
    matched = [name for name in SITES if name in cleaned]

    if matched:
        opened = []
        for name in matched:
            webbrowser.open(SITES[name])
            opened.append(name.capitalize())
        return "Opened " + ", ".join(opened) + "."

    # 2. Raw URL or bare domain?
    url_match = _URL_RE.search(cleaned)

    if url_match:
        url = url_match.group(0)
        if not url.startswith("http"):
            url = "https://" + url
        webbrowser.open(url)
        return f"Opened {url}."

    # 3. Fall back to a browser search.
    search_term = cleaned.strip()

    if not search_term:
        return "What would you like me to open?"

    webbrowser.open(SEARCH_URL.format(query=quote_plus(search_term)))
    return f"Searching the web for '{search_term}'."
