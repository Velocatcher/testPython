from list_notes import list_notes

def filter_notes_by_date(notes):
    date_filter = input("Введите дату в формате (YYYY-MM-DD) для фильтрации заметок: ")
    filtered_notes = [note for note in notes if note["created_at"].startswith(date_filter)]
    list_notes(filtered_notes)