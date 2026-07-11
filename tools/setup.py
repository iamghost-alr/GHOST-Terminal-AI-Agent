import os
import webbrowser
import subprocess

from config import APPS, SITES, SETUPS, DEFAULT_SETUP


def _resolve_bundle(query):
    """Pick the setup bundle the user is asking for.

    Returns the bundle name (a key of SETUPS), or None if it doesn't exist.
    """

    text = query.lower()

    # Did the user name a specific bundle?
    for name in SETUPS:
        if name in text:
            return name

    # Otherwise use the configured default.
    return DEFAULT_SETUP


def run_setup(query):
    """Initialize a predefined setup: launch its apps and open its sites."""

    bundle_name = _resolve_bundle(query)
    bundle = SETUPS.get(bundle_name)

    if not bundle:
        available = ", ".join(SETUPS) or "(none configured)"
        return f"No setup called '{bundle_name}'. Available: {available}."

    opened = []

    # Launch apps.
    for app_key in bundle.get("apps", []):
        path = APPS.get(app_key)
        if not path:
            opened.append(f"{app_key} (not configured)")
            continue
        if not os.path.exists(path):
            opened.append(f"{app_key} (path not found)")
            continue
        try:
            subprocess.Popen([path])
            opened.append(app_key.capitalize())
        except Exception as e:
            opened.append(f"{app_key} (failed: {e})")

    # Open sites.
    for site_key in bundle.get("sites", []):
        url = SITES.get(site_key)
        if not url:
            opened.append(f"{site_key} site (not configured)")
            continue
        try:
            webbrowser.open(url)
            opened.append(site_key.capitalize())
        except Exception as e:
            opened.append(f"{site_key} site (failed: {e})")

    summary = ", ".join(opened) if opened else "nothing"
    return f"Setup '{bundle_name}' initialized: {summary}."
