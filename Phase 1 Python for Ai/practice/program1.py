import os

file_path = "Phase 1 Python for Ai/practice/note.txt"

def menu():
    print("1. Write a Note")
    print("2. Read Notes")
    print("3. Delete all Notes")
    print("4. Exit")

while(True):
    menu()
    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("\nNot a Number\n")
        continue

    choice = int(choice)

    if choice == 1:
        note = input("\nEnter your Note: ")
        with open(file_path, "a") as file:
            file.write(f"{note}\n")
        print("Note added to your Notebook\n")

    elif choice == 2:
        with open(file_path, "r") as file:
            for i, line in enumerate(file, 1):
                print(f"{i}. {line}", end="")
        print("\n")

    elif  choice == 3:
         """Delete all notes"""
         confirm = input("Delete all notes? (yes/no): ")
         if(confirm.lower() == "yes"):
             try:
                 os.remove(file_path)
                 print("All notes deleted")
             except FileNotFoundError:
                 print("No notes to delete")
    elif choice == 4:
         print("Goodbye!")
         break
    else:
        print("Invalid input")


