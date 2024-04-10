import json

def load_notes():
    
    try:
        with open("db/notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes    