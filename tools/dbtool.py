from database.db import save_memory, get_memories

def memory_tool(query):

    query = query.lower().strip()

    if query.startswith("save memory"):

        memory = query.replace(
            "save memory",
            ""
        ).strip()

        save_memory(memory)

        return "Memory saved successfully"

    elif query in [
        "show memories",
        "get all memories"
    ]:

        return get_memories()

    else:

        return {
            "type": "memory",
            "data": get_memories()
        }