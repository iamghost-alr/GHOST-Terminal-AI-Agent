from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
from os import getenv

load_dotenv()

client = MongoClient(getenv("MONGO_DB_URI"))
print("\n Database Connected \n")

db = client.ghost_memory
memories = db.memories


def save_memory(content, memory_type="general"):
    memories.insert_one({
        "content": content,
        "type": memory_type,
        "timestamp": datetime.now().strftime("%d-%m-%Y | %H:%M:%S")
    })


def get_memories(limit=20):
    return list(
        memories.find(
            {},
            {"_id": 0}
        ).limit(limit)
    )
