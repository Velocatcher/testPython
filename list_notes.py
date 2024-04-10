
def list_notes(notes):
    
    if not notes:
        print("Таких заметок нет\n")
        return
    for note in notes:
        print(f'ID: {note["id"]} | Заголовок: {note["title"]} | Тело: {note["body"]} | Создана: {note["created_at"]}\n')
        if "updated_at" in note:
            print(f'Последнее изменение: {note["updated_at"]}\n')
