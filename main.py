from crud import *


def menu():
    print("\n--- Library CLI ---")
    print("1. Add Author")
    print("2. Add Book")
    print("3. List Authors")
    print("4. List Books")
    print("5. Update Author")
    print("6. Update Book")
    print("7. Delete Author")
    print("8. Delete Book")
    print("9. Exit")
    return input("\nChoose an option: ")


def main():
    while True:
        choice = menu()
        if choice == "1":
            add_author()
        elif choice == "2":
            add_book()
        elif choice == "3":
            list_authors()
        elif choice == "4":
            list_books()
        elif choice == "5":
            update_author()
        elif choice == "6":
            update_book()
        elif choice == "7":
            delete_author()
        elif choice == "8":
            delete_book()
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    main()
