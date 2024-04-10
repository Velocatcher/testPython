from ui import start_menu
from load_notes import load_notes


if __name__ == "__main__":
        notes = load_notes() 
        start_menu(notes)
    
