from tavily import TavilyClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

tavily = TavilyClient(api_key=getenv("TAVILY_API_KEY"))

def web_search(query):
    try:
        response = tavily.search(query=query)

        results = response.get("results", [])

        if not results:
            return "No result found"

        formatted = []

        for i, r in enumerate(results[:3], 1):
            title = r.get("title", "No title")
            url = r.get("url", "No url")
            content = r.get("content", "No content")

            formatted.append(
                f"{i}. {title}\n{content}\nSource: {url}"
            )

        return "\n\n".join(formatted)

    except Exception as e:
        return f"Search error: {e}"