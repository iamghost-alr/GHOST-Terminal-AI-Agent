import re

from textblob import TextBlob

from tools.calculator import calculator
from tools.time import check_time, check_date
from tools.notes import save_note, show_notes, clear_notes
from tools.weather import check_weather
from tools.web_search import web_search
from tools.dbtool import save_memory, get_memories
import webbrowser

operator_map = {
    "plus": "add",
    "add": "add",
    "minus": "sub",
    "subtract": "sub",
    "multiply": "mul",
    "divide": "div",
    "power": "pow",
    "times": "mul"
}

math_keywords = [
    "plus",
    "add",
    "minus",
    "subtract",
    "multiply",
    "divide",
    "power",
    "times"
]

memory_keywords = [
    "my name",
    "who am i",
    "remember me",
    "what do you know about me",
    "what can you tell about me",
    "memory",
    "show memories",
    "remember this",
    "what do i like",
    "what do i hate",
    "what are my habits",
    "tell me about myself"
]

sites = ["google", "youtube", "instagram", "facebook", "twitter", "tiktok"]


def tool_router(user_input):

    # MATH TOOL
    if any(op in user_input.lower() for op in math_keywords):

        try:

            text = user_input.lower().strip()

            for w in ["what is", "calculate", "simple", "and"]:
                text = text.replace(w, "")

            tokens = re.findall(
                r"(\d+|plus|minus|multiply|divide|add|subtract|[+\-*/])",
                text
            )

            numbers = []
            operators = []

            for token in tokens:

                if token.isdigit():
                    numbers.append(int(token))

                else:
                    operators.append(token)

            if len(numbers) != 2:
                return "Invalid math input."

            if len(operators) != 1:
                return "Invalid math input."

            operator = operators[0]

            if operator in operator_map:
                operator = operator_map[operator]

            a = numbers[0]
            b = numbers[1]

            result = calculator(a, b, operator)

            return str(result)

        except Exception:
        
            return "Invalid math input."


    # TIME TOOL
    elif "time" in user_input:

        return check_time()


    # DATE TOOL
    elif "date" in user_input:

        return check_date()

    # SHOW NOTES
    elif "show notes" in user_input.lower():
        return show_notes()

    # CLEAR NOTES
    elif "clear notes" in user_input.lower():
        return clear_notes()

    # SAVE NOTE
    elif "note" in user_input.lower():

        note = (
            user_input
            .replace("note", "")
            .replace("a note", "")
            .strip()
        )

        return save_note(note)

    #WEATHER TOOL

    elif "weather" in user_input:

        city = (user_input
        .replace("weather","")
        .replace("in","")
        .replace("the","")
        .replace("what","")
        .replace("is","")
        .replace("show","")
        .strip()
        )

        return check_weather(city)

    elif "search" in user_input:

        query = user_input.replace("search","",).replace("about","",).strip()

        return web_search(query)

    ## MEMORY TOOL

    elif "save memory" in user_input.lower() or "remember this" in user_input.lower():

        memory = (
            user_input
            .lower()
            .replace("save memory", "")
            .replace("remember this", "")
            .replace("?","")
            .replace("!")
            .replace(".")
            .replace(" ")
        .strip()
    )

        return save_memory(memory)

    elif any(
        keyword in user_input.lower()
        for keyword in memory_keywords
    ):

        return {
            "type" : "memory",
            "data" : get_memories()
        }

        

    # NO TOOL MATCHED
    return None
