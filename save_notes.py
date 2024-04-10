import json

def save_notes(notes):
    with open("db/notes.json", "w") as file:
        json.dump(notes, file, indent=4)
           