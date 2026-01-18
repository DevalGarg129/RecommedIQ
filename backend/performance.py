import json
import os

DB_PATH = "db/db.json"

def load_db():
    if not os.path.exists(DB_PATH):
        return {"users": {}}
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

def load_user_progress(user_id: int):
    db = load_db()
    uid = str(user_id)

    # If user doesn't exist yet
    if uid not in db["users"]:
        db["users"][uid] = {"last_id": 0}

    return db["users"][uid]

def save_user_progress(user_id: int, material: str):
    db = load_db()
    uid = str(user_id)

    if uid not in db["users"]:
        db["users"][uid] = {"last_id": 0}

    # increment content id by 1 (simple rule)
    db["users"][uid]["last_id"] += 1

    save_db(db)
