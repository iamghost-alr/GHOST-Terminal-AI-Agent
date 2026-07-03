import subprocess

apps = {
    "antigravity" : "C:/Users/naman/AppData/Local/Programs/Antigravity IDE/Antigravity IDE.exe",
    "postman" : "C:/Users/naman/AppData/Local/Postman/Postman.exe",
    "terminal" : "C:/Program Files/WindowsApps/Microsoft.WindowsTerminal_1.24.11321.0_x64__8wekyb3d8bbwe",
    "brave" : "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe",
    "calculator" : "C:/Windows/System32/calc.exe",
    "mongo db" : "C:/Users/naman/AppData/Local/MongoDBCompass/MongoDBCompass.exe"
}

def open_app(query):
    query = (
        query.lower()
        .replace("open", "")
        .replace("application", "")
        .replace("app", "")
        .replace("in", "")
        .replace("the", "")
        .replace("what", "")
        .replace("is", "")
        .replace("show", "")
        .strip()
    )

    for app in apps:
        if app in query:
            subprocess.Popen(apps[app])
            return f"{app} opened successfully"

    return "Application not found"