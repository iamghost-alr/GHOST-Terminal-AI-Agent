def save_note(note):
    try:
        with open("memory/notes.txt", "a") as file:
            file.write(note + "\n")
            return "Note saved successfully"
    except Exception as e:
        return f"Error: {e}"

def show_notes():

    try:

        with open("memory/notes.txt", "r") as file:
            notes = file.read()

        if notes.strip() == "":
            return "No notes found"

        return notes

    except FileNotFoundError:
        return "No notes file found"

    except Exception as e:
        return f"Error: {e}"

def clear_notes():

    try:

        with open("memory/notes.txt", "w") as file:
            file.write("")

        return "Notes cleared successfully"

    except Exception as e:
        return f"Error: {e}"