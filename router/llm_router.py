import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()

api_key = getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "deepseek/deepseek-chat-v3.1"

# Tools the router is allowed to pick from. Must stay in sync with
# the dispatch table in router/tool_router.py.
VALID_TOOLS = [
    "calculator",
    "time",
    "date",
    "notes",
    "weather",
    "web_search",
    "sites",
    "application",
    "memory",
    "none",
]

ROUTER_PROMPT = """You are a routing engine for an AI assistant named GHOST.

Pick exactly ONE tool from this list that should handle the user's query.

TOOLS:
- calculator : math (add, subtract, multiply, divide, power, percentages, etc.)
- time       : current time
- date       : current date or day of the week
- notes      : saving, showing, or clearing notes/reminders
- weather    : weather conditions for a location
- web_search : look something up on the internet
- sites      : open a specific website (youtube, google, github, ...)
- application: open a desktop application (calculator, browser, editor, ...)
- memory     : save something about the user OR recall stored user facts
- none       : general conversation / none of the above

RULES:
- Return ONLY the tool name, one lowercase word, nothing else.
- Tolerate spelling mistakes and typos (e.g. "calulate", "weathr", "serch",
  "pluus", "remeber"). Understand the user's intent, not just the literal words.
- If the query is casual chat, greetings, opinions, explanations, or anything
  not covered above, return: none

User query:
"""


def route_query(query):
    """Ask the LLM which tool should handle the query.

    Returns a single tool name from VALID_TOOLS, or "none" on any failure
    (so the caller gracefully falls through to the chat API).
    """

    try:

        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/GHOST-Terminal-AI-Agent",
                "X-Title": "GHOST Terminal AI",
            },
            json={
                "model": MODEL,
                "temperature": 0,
                "max_tokens": 5,
                "messages": [
                    {
                        "role": "user",
                        "content": ROUTER_PROMPT + query,
                    }
                ],
            },
            timeout=20,
        )

        if response.status_code != 200:
            return "none"

        tool = (
            response.json()["choices"][0]["message"]["content"]
            .strip()
            .lower()
        )

        # The model occasionally adds punctuation/quotes; grab first token.
        tool = tool.split()[0].strip(".\"'!,;:")

        if tool not in VALID_TOOLS:
            return "none"

        return tool

    except Exception:
        return "none"
