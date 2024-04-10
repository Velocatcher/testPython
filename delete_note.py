from save_notes import save_notes

def delete_note(notes):
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена\n")
            return
    print("Заметка с таким ID не найдена\n")