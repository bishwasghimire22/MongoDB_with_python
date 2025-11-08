from bson.objectid import ObjectId
from database import db


# ---------- CREATE ----------
def add_author():
    name = input("Author name: ")
    if db.authors.find_one({"name": name}):
        print(f"Author '{name}' already exists.")
        return
    db.authors.insert_one({"name": name})
    print(f"Author '{name}' added successfully!")


def add_book():
    title = input("Book title: ")
    if db.books.find_one({"title": title}):
        print(f"Book '{title}' already exists.")
        return

    author_name = input("Author name: ")
    author = db.authors.find_one({"name": author_name})
    if not author:
        print(f"Author '{author_name}' not found. Add the author first.")
        return

    year = int(input("Year: "))
    categories = input("Categories (comma-separated): ").split(",")
    copies = int(input("Number of copies: "))
    ebook_input = input("Is it an ebook? (y/n): ").lower()
    ebook = True if ebook_input == "y" else False

    book = {
        "title": title,
        "author_id": author["_id"],  # store reference
        "year": year,
        "categories": [c.strip() for c in categories],
        "copies": copies,
        "ebook": ebook,
    }

    db.books.insert_one(book)
    print(f"Book '{title}' added successfully!")


# ---------- READ ----------
def list_authors():
    print("\nAuthors:")
    for author in db.authors.find():
        print(f"- {author['name']}")


def list_books():
    print("\nBooks:")
    for book in db.books.find():
        author = db.authors.find_one({"_id": book["author_id"]})
        author_name = author["name"] if author else "Unknown"
        print(f"- {book['title']} by {author_name} ({book['year']})")
        print(f"  Categories: {', '.join(book['categories'])}")
        print(f"  Copies: {book['copies']}, Ebook: {book['ebook']}\n")


# ---------- UPDATE ----------
def update_author():
    old_name = input("Author name to update: ")
    author = db.authors.find_one({"name": old_name})
    if not author:
        print(f"Author '{old_name}' not found.")
        return

    new_name = input("New author name: ")
    db.authors.update_one({"_id": author["_id"]}, {"$set": {"name": new_name}})
    print(f"Author '{old_name}' updated to '{new_name}'.")


def update_book():
    title = input("Book title to update: ")
    book = db.books.find_one({"title": title})
    if not book:
        print(f"Book '{title}' not found.")
        return

    new_title = input(f"New title ({book['title']}): ") or book["title"]

    # Author update
    author_name = input("New author name (leave blank to keep current): ")
    if author_name:
        author = db.authors.find_one({"name": author_name})
        if not author:
            print(f"Author '{author_name}' not found. Add the author first.")
            return
        author_id = author["_id"]
    else:
        author_id = book["author_id"]

    year = input(f"New year ({book['year']}): ") or book["year"]
    categories = input(
        f"New categories (comma-separated) ({', '.join(book['categories'])}): "
    )
    copies = input(f"New copies ({book['copies']}): ") or book["copies"]
    ebook_input = input(f"Is it an ebook? (y/n) ({book['ebook']}): ").lower()

    updated_book = {
        "title": new_title,
        "author_id": author_id,
        "year": int(year),
        "categories": (
            [c.strip() for c in categories.split(",")]
            if categories
            else book["categories"]
        ),
        "copies": int(copies),
        "ebook": (
            True
            if ebook_input == "y"
            else (False if ebook_input == "n" else book["ebook"])
        ),
    }

    db.books.update_one({"_id": book["_id"]}, {"$set": updated_book})
    print(f"Book '{title}' updated successfully.")


# ---------- DELETE ----------
def delete_author():
    name = input("Author name to delete: ")
    author = db.authors.find_one({"name": name})
    if not author:
        print(f"Author '{name}' not found.")
        return
    db.books.delete_many({"author_id": author["_id"]})
    db.authors.delete_one({"_id": author["_id"]})
    print(f"Author '{name}' and all their books deleted.")


def delete_book():
    title = input("Book title to delete: ")
    book = db.books.find_one({"title": title})
    if not book:
        print(f"Book '{title}' not found.")
        return
    db.books.delete_one({"_id": book["_id"]})
    print(f"Book '{title}' deleted successfully.")
