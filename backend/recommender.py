import json
import random

DATA_PATH = "data/content.json"

def recommend(progress):
    with open(DATA_PATH, "r") as f:
        materials = json.load(f)

    item = random.choice(materials)
    return f"{item['topic']}\nLink: {item['link']}"
