import re

from tools.calculator import calculator, operator_map
from tools.time import check_time, check_date
from tools.notes import save_note, show_notes, clear_notes
from tools.weather import check_weather
from tools.web_search import web_search
from tools.sites import open_sites
from tools.dbtool import save_memory, get_memories
from tools.application import open_app
from tools.setup import run_setup

# Words that should be stripped out of a math query before parsing.
MATH_FILLER = ["what is", "calculate", "simple", "and", "whats"]


def _handle_calculator(query):

    try:

        text = query.lower().strip()

        for word in MATH_FILLER:
            text = text.replace(word, "")

        # Numbers, word-operators and symbol-operators.
        tokens = re.findall(
            r"(\d+(?:\.\d+)?|plus|minus|multiply|divide|add|subtract|"
            r"times|power|sub|mul|div|pow|[+\-*/^])",
            text,
        )

        numbers = []
        operators = []

        for token in tokens:
            if re.match(r"\d+(?:\.\d+)?", token):
                numbers.append(float(token) if "." in token else int(token))
            else:
                operators.append(token)

        if len(numbers) != 2 or len(operators) != 1:
            return "I couldn't understand that calculation. " \
                   "\nTry something like '12 plus 8' or '15 * 3'."

        return str(calculator(numbers[0], numbers[1], operators[0]))

    except Exception as e:
        return f"Calculation error: {e}\n\nTry again"


def _handle_notes(query):

    q = query.lower()

    if "clear" in q:
        return clear_notes()

    if "show" in q or "list" in q or "all" in q:
        return show_notes()

    # Default: treat the rest of the query as a note to save.
    note = query.lower()
    for word in ["note", "a note", "save", "take", "remind"]:
        note = note.replace(word, "")
    note = note.strip()

    if not note:
        return "What would you like me to note?"

    return save_note(note)


def _handle_weather(query):

    city = query.lower()
    for word in [
        "weather", "in", "the", "what", "is", "show",
        "like", "today", "outside", "of", "tell", "me", "and",
    ]:
        city = city.replace(word, "")
    city = city.strip()

    if not city:
        return "Which city's weather would you like?"

    return check_weather(city)


def _handle_web_search(query):

    q = query.lower()
    for word in ["search", "about", "for", "the", "google", "look", "up"]:
        q = q.replace(word, "")
    q = q.strip()

    if not q:
        return "What should I search for?"

    return web_search(q)


def _handle_sites(query):

    return open_sites(query)


def _handle_application(query):

    app = query.lower()
    for word in [
        "open", "launch", "start", "access",
        "application", "app", "the", "for", "me",
    ]:
        app = app.replace(word, "")
    app = app.strip()

    if not app:
        return "Which application should I open?"

    return open_app(app)


def _handle_memory(query):

    q = query.lower()

    # Saving a new memory.
    if "save" in q or "remember" in q or "store" in q:

        memory = q
        for phrase in [
            "save memory", "save", "remember this", "remember",
            "store", "this", "that", "please",
        ]:
            memory = memory.replace(phrase, "")
        memory = memory.strip(" .!?,")

        if not memory:
            return "What should I remember?"

        save_memory(memory)
        return "Got it. That's saved to memory."

    # Otherwise recall stored memories and present them directly
    # (no chat API needed).
    memories = get_memories()

    if not memories:
        return "I don't have any memories stored yet."

    lines = [f"- {m['content']}" for m in memories]
    return "Here's what I know about you:\n" + "\n".join(lines)


def _handle_setup(query):

    return run_setup(query)


# Dispatch table: tool name -> handler.
# Keep the keys in sync with VALID_TOOLS in router/llm_router.py
# (minus "none", which never reaches here).
_DISPATCH = {
    "calculator": _handle_calculator,
    "time": lambda q: check_time(),
    "date": lambda q: check_date(),
    "notes": _handle_notes,
    "weather": _handle_weather,
    "web_search": _handle_web_search,
    "sites": _handle_sites,
    "application": _handle_application,
    "setup": _handle_setup,
    "memory": _handle_memory,
}


def tool_router(tool_name, query):
    """Run the tool selected by the LLM router.

    Returns a ready-to-show string, or None if the tool name is unknown /
    'none' (so the caller falls back to the chat API).
    """

    handler = _DISPATCH.get(tool_name)

    if handler is None:
        return None

    try:
        return handler(query)

    except Exception as e:
        return f"Tool error: {e}"
