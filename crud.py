from bson.objectid import ObjectId
from database import db

# ---------- CREATE ----------
def add_author(name):
    author = {"name": name}
    result = db.authors.insert_one(author)
    print(f"Author added with ID: {result.inserted_id}")

def add_book(title, author_name):
    author = db.authors.find_one({"name": author_name})
    if not author:
        print("Author not found! Add the author first.")
        return
    book = {"title": title, "author": author["_id"]}
    result = db.books.insert_one(book)
    print(f"Book added with ID: {result.inserted_id}")

# ---------- READ ----------
def list_authors():
    for author in db.authors.find():
        print(f"{author['_id']}: {author['name']}")

def list_books():
    for book in db.books.find():
        author = db.authors.find_one({"_id": book["author"]})
        author_name = author["name"] if author else "Unknown"
        print(f"{book['_id']}: {book['title']} (Author: {author_name})")

# ---------- UPDATE ----------
def update_author(author_id, new_name):
    db.authors.update_one({"_id": ObjectId(author_id)}, {"$set": {"name": new_name}})
    print("Author updated.")

def update_book(book_id, new_title):
    db.books.update_one({"_id": ObjectId(book_id)}, {"$set": {"title": new_title}})
    print("Book updated.")

# ---------- DELETE ----------
def delete_author(author_id):
    db.authors.delete_one({"_id": ObjectId(author_id)})
    print("Author deleted.")

def delete_book(book_id):
    db.books.delete_one({"_id": ObjectId(book_id)})
    print("Book deleted.")
