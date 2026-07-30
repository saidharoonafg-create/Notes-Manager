# File name: notes_manager.py

FILE_NAME = "notes.txt"

def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("✅ Note saved successfully!\n")


def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()
            if not notes:
                print("⚠️ No notes found.\n")
            else:
                print("\n📒 Your Notes:")
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")
                print()
    except FileNotFoundError: 
        print("⚠️ No notes file found yet.\n")


def main():
    while True:
        print("==== Notes Manager ====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()