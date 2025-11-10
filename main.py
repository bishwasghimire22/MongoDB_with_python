from crud import *


def menu():
    print("\n--- Movie Database CLI ---")
    print("1. Add Director")
    print("2. Add Movie")
    print("3. List Directors")
    print("4. List Movies")
    print("5. Update Director")
    print("6. Update Movie")
    print("7. Delete Director")
    print("8. Delete Movie")
    print("9. View Director Details")
    print("10. Exit")
    return input("\nChoose an option: ")


def main():
    while True:
        choice = menu()
        if choice == "1":
            add_director()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            list_directors()
        elif choice == "4":
            list_movies()
        elif choice == "5":
            update_director()
        elif choice == "6":
            update_movie()
        elif choice == "7":
            delete_director()
        elif choice == "8":
            delete_movie()
        elif choice == "9":
            view_director_details()
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    main()
