import os
import json

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    return {}

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=2)

def list_notes(notes):
    if not notes:
        print("\nNo notes found.")
        return
    print("\nAll Notes:")
    for i, title in enumerate(notes.keys(), 1):
        print(f"{i}. {title} ({notes[title]['category']})")

def view_note(notes):
    title = input("Enter the title of the note you want to view: ").strip()
    if title in notes:
        print(f"\n--- {title} ---")
        print(f"Category: {notes[title]['category']}")
        print(notes[title]['content'])
    else:
        print("Note not found.")

def add_or_edit_note(notes):
    title = input("Enter the title of the note: ").strip()
    category = input("Enter the category for this note: ").strip()
    print("Enter your note content (end with a blank line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    content = "\n".join(lines)
    notes[title] = {"category": category, "content": content}
    print("Note saved.")

def delete_note(notes):
    title = input("Enter the title of the note to delete: ").strip()
    if title in notes:
        del notes[title]
        print("Note deleted.")
    else:
        print("Note not found.")

def search_notes(notes):
    keyword = input("Enter a keyword to search for: ").strip().lower()
    results = [
        (title, data) for title, data in notes.items()
        if keyword in title.lower() or keyword in data["content"].lower()
    ]
    if results:
        print(f"\nFound {len(results)} note(s):")
        for title, data in results:
            print(f"\n--- {title} ({data['category']}) ---\n{data['content']}")
    else:
        print("No matching notes found.")

def list_by_category(notes):
    category = input("Enter the category name: ").strip().lower()
    matches = {title: data for title, data in notes.items() if data["category"].lower() == category}
    if matches:
        print(f"\nNotes in '{category}' category:")
        for title, data in matches.items():
            print(f"\n--- {title} ---\n{data['content']}")
    else:
        print("No notes found in that category.")

def main():
    notes = load_notes()
    while True:
        print("\n--- Note Taking App ---")
        print("1. List all notes")
        print("2. View a note")
        print("3. Add/Edit a note")
        print("4. Delete a note")
        print("5. Search notes")
        print("6. List notes by category")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()
        if choice == "1":
            list_notes(notes)
        elif choice == "2":
            view_note(notes)
        elif choice == "3":
            add_or_edit_note(notes)
            save_notes(notes)
        elif choice == "4":
            delete_note(notes)
            save_notes(notes)
        elif choice == "5":
            search_notes(notes)
        elif choice == "6":
            list_by_category(notes)
        elif choice == "7":
            save_notes(notes)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
