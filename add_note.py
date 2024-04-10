import datetime
from save_notes import save_notes

def add_note(notes):
    note_id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append({"id": note_id, "title": title, "body": body, "created_at": created_at})
    save_notes(notes)
    print("Заметка успешно добавлена\n")