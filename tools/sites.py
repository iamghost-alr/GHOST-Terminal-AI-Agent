import webbrowser 
from tools.web_search import web_search

sites = {
    "google": "www.google.com",
    "youtube": "www.youtube.com",
    "instagram": "www.instagram.com",
    "facebook": "www.facebook.com",
    "twitter": "www.twitter.com",
    "brave": "www.brave.com",
    "github": "www.github.com",
    "claude": "www.claude.com",
    "chatgpt": "www.chatgpt.com",
    "amazon": "www.amazon.com",
    "flipkart": "www.flipkart.com"
    
 }

def open_sites(user_input):
    query = (
        user_input.lower()
        .replace("open", "")
        .replace("sites", "")
        .replace("in", "")
        .replace("the", "")
        .replace("what", "")
        .replace("is", "")
        .replace("show", "")
        .strip()
    )

    for site in sites:
        if site in query:
            webbrowser.open(sites[site])
            return f"{site.capitalize()} opened successfully"

    result = web_search(query)
    return f"{result}\n\nHere's what I found about '{query}'."
