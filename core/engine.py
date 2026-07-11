import requests
from dotenv import load_dotenv
from os import getenv

from voice.tts import clean_response, speak, stop_speaking
from router.llm_router import route_query
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


class GhostEngine:

    def __init__(self):

        self.custom_prompt = """
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

        self.API_KEY = getenv("OPENROUTER_API_KEY")

        if not self.API_KEY:
            show_error("OPENROUTER_API_KEY not found in .env file")
            raise SystemExit

        self.chat_history = []
        self.MAX_HISTORY = 20

    def run(self):

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

            self.chat_history.append(
                {
                    "role": "user",
                    "content": query
                }
            )

            if len(self.chat_history) > self.MAX_HISTORY:
                self.chat_history = self.chat_history[-self.MAX_HISTORY:]

            try:

                # --- LLM brain: decide which tool (if any) handles this ---
                tool_name = route_query(query)

                tool_response = None

                if tool_name != "none":
                    tool_response = tool_router(tool_name, query)

                # --- Tool hit: answer locally, NO chat API call ---
                if tool_response:

                    tool_used(tool_name)

                    cleaned = clean_response(str(tool_response))

                    ai_response(cleaned)

                    speak(cleaned)

                    self.chat_history.append(
                        {
                            "role": "assistant",
                            "content": str(tool_response)
                        }
                    )

                # --- No tool matched: fall back to the chat API ---
                else:

                    thinking()

                    messages = [
                        {
                            "role": "system",
                            "content": self.custom_prompt
                        }
                    ] + self.chat_history

                    headers = {
                        "Authorization": f"Bearer {self.API_KEY}",
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

                    self.chat_history.append(
                        {
                            "role": "assistant",
                            "content": reply
                        }
                    )

            except Exception as e:
                show_error(str(e))

            divider()