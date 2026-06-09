import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()

api_key = getenv("OPENROUTER_API_KEY")


def route_query(query):

    router_prompt = router_prompt = f"""
You are a routing engine.

Available tools:

dbtool
weather
notes
time
web_search
none

Rules:

- Questions about user facts -> dbtool
- Questions about saved information -> dbtool
- Weather queries -> weather
- Notes related actions -> notes
- Current time/date -> time
- Internet knowledge -> web_search
- General conversation -> none

Return ONLY one tool name.

User Query:
{query}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-chat-v3.1",
            "messages": [
                {
                    "role": "user",
                    "content": router_prompt
                }
            ]
        }
    )

    tool = response.json()["choices"][0]["message"]["content"]

    return tool.strip().lower()