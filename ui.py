from add_note import add_note 
from edit_note import edit_note
from delete_note import delete_note
from list_notes import list_notes
from check_number import check_number
from filter_notes_by_date import filter_notes_by_date

def start_menu(notes):
    command = None
    while command != 6:
        command = int(input("Выберите пункт меню:\n"
                            "1. Добавить заметку\n"
                            "2. Редактировать заметку\n"
                            "3. Удалить заметку\n"
                            "4. Вывести список заметок\n"
                            "5. Фильтрация заметок по дате\n"
                            "6. Выйти\n"
                            "Введите номер команды: "))
        command = check_number(command)
        if command == 1:
            add_note(notes)
        elif command == 2:
            edit_note(notes)
        elif command == 3:
            delete_note(notes)
        elif command == 4:
            list_notes(notes)
        elif command == 5:
            filter_notes_by_date(notes)    
    print("\nСпасибо, что воспользовались нашими услугами!\n"
          "Всего доброго! Приходите к нам ещё :)\n")