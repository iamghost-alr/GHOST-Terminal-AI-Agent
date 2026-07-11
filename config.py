"""
GHOST configuration.

Everything GHOST can launch lives here. Edit this file to add, rename,
or remove apps, sites, and setup bundles — no code changes required.
"""

# ---------------------------------------------------------------------------
# DESKTOP APPLICATIONS
# The name you say (lowercase)  ->  the .exe path GHOST launches.
# ---------------------------------------------------------------------------
APPS = {
    "antigravity": "C:/Users/naman/AppData/Local/Programs/Antigravity IDE/Antigravity IDE.exe",
    "zcode":       "C:/Users/naman/AppData/Local/Programs/ZCode/ZCode.exe",
    "brave":       "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe",
    "calculator":  "C:/Windows/System32/calc.exe",
    "postman":     "C:/Users/naman/AppData/Local/Postman/Postman.exe",
    "mongodb":     "C:/Users/naman/AppData/Local/MongoDBCompass/MongoDBCompass.exe",
}

# ---------------------------------------------------------------------------
# WEBSITES
# The name you say (lowercase)  ->  the URL opened in the browser.
# ---------------------------------------------------------------------------
SITES = {
    "google":   "https://google.com",
    "youtube":  "https://youtube.com",
    "github":   "https://github.com",
    "claude":   "https://claude.com",
    "chatgpt":  "https://chatgpt.com",
    "amazon":   "https://amazon.com",
    "flipkart": "https://flipkart.com",
}

# ---------------------------------------------------------------------------
# SETUP BUNDLES
# "initialize my setup" / "start my dev environment" opens one of these.
# Each bundle can launch apps (by APPS key) and sites (by SITES key).
# ---------------------------------------------------------------------------
SETUPS = {
    "dev": {
        "apps":  ["antigravity", "zcode", "brave"],
        "sites": [],
    },
    "coding": {
        "apps":  ["antigravity", "zcode"],
        "sites": ["github"],
    },
}

# Which bundle runs when the user just says "initialize my setup".
DEFAULT_SETUP = "dev"

# Template used when the user asks to open something that isn't a known
# site or a raw URL — it becomes a browser search.
SEARCH_URL = "https://www.google.com/search?q={query}"
