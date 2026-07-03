import requests
from dotenv import load_dotenv
from os import getenv
from voice.tts import clean_response, speak, stop_speaking
from router.tool_router import tool_router

from ui.terminal_ui import (
    show_banner,
    startup,
    divider,
    user_input,
    ai_response,
    thinking,
    warning,
    show_error,
    tool_used
)

load_dotenv()

custom_prompt = """
You are GHOST, an advanced AI assistant. 

Your personality, communication style, professionalism, intelligence, and subtle humor should be inspired by JARVIS from Iron Man.

Be calm, composed, intelligent, efficient, and reliable. Speak naturally and confidently. Prioritize accuracy, usefulness, and clarity.

Use concise responses for simple tasks and detailed explanations for complex ones. For coding and technical problems, provide practical solutions, identify issues logically, and suggest improvements when relevant.

Maintain a professional and sophisticated demeanor at all times. Be polite without being overly formal. Be confident without being arrogant.

You may occasionally use dry, intelligent sarcasm or subtle wit when appropriate. Your humor should be understated, well-timed, and never disrespectful. Do not force jokes into every response.

Avoid excessive enthusiasm, unnecessary apologies, filler phrases, roleplay, or emotional overreactions. Stay focused on helping the user efficiently.

Act like a highly capable AI operating system: observant, resourceful, analytical, and dependable. Your goal is to help the user solve problems, learn, build, and make informed decisions.

When speaking, keep responses concise and natural.

Avoid long lists unless necessary.

Prefer conversational sentences over markdown formatting.

You are GHOST.
"""

API_KEY = getenv("OPENROUTER_API_KEY")

if not API_KEY:
    show_error("OPENROUTER_API_KEY not found in .env file")
    raise SystemExit

chat_history = []
MAX_HISTORY = 20

def main():

    global chat_history

    show_banner()
    startup()
    divider()

    while True:

        user_input()
        query = input().strip()

        if query.lower() in ["quit", "exit"]:
            warning("Shutting down GHOST...")
            break

        divider()

        chat_history.append(
            {
                "role": "user",
                "content": query
            }
        )

        if len(chat_history) > MAX_HISTORY:
            chat_history = chat_history[-MAX_HISTORY:]

        try:

            tool_response = tool_router(query)

            if tool_response:

                if (
                    isinstance(tool_response, dict)
                    and tool_response.get("type") == "memory"
                ):

                    memories = tool_response["data"]

                    memory_context = "\n".join(
                        [
                            memory["content"]
                            for memory in memories
                        ]
                    )

                    messages = [
                        {
                            "role": "system",
                            "content": custom_prompt
                        },
                        {
                            "role": "system",
                            "content": f"""
                            Relevant user memories:

                            {memory_context}

                            Use these memories when answering.
                            """
                        },
                        {
                            "role": "user",
                            "content": query
                        }
                    ]

                    payload = {
                        "model": "deepseek/deepseek-chat-v3.1",
                        "messages": messages
                    }

                    headers = {
                        "Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json",
                        "HTTP-Referer": "https://github.com/GHOST-Terminal-AI-Agent",
                        "X-Title": "GHOST Terminal AI"
                    }

                    response = requests.post(
                        url="https://openrouter.ai/api/v1/chat/completions",
                        headers=headers,
                        json=payload,
                        timeout=60
                    )

                    reply = response.json()["choices"][0]["message"]["content"]

                    cleaned = clean_response(reply)

                    ai_response(cleaned)

                    speak(cleaned)

                else:

                    tool_used("Utility")

                    cleaned = clean_response(str(tool_response))

                    ai_response(cleaned)

                    speak(cleaned)

            else:

                thinking()

                messages = [
                    {
                        "role": "system",
                        "content": custom_prompt
                    }
                ] + chat_history

                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://github.com/GHOST-Terminal-AI-Agent",
                    "X-Title": "GHOST Terminal AI"
                    }

                payload = {
                    "model": "deepseek/deepseek-chat-v3.1",
                    "messages": messages
                }

                response = requests.post(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=60
                )

                if response.status_code != 200:
                    show_error(
                        f"HTTP {response.status_code}: {response.text}"
                    )
                    divider()
                    continue

                data = response.json()

                if "choices" not in data:
                    show_error(
                        f"API error: {data.get('error', {}).get('message', str(data))}"
                    )
                    divider()
                    continue

                reply = data["choices"][0]["message"]["content"]

                cleaned = clean_response(reply)

                ai_response(cleaned)

                speak(cleaned)

                chat_history.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        except Exception as e:
            show_error(str(e))

        divider()

if __name__ == "__main__":
    main()