from pymongo import MongoClient
import os

# Use local MongoDB or environment variable
MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)

db = client["library"]

# Clear existing data (optional, for testing)
###  db.authors.delete_many({})
#### db.books.delete_many({})

# Sample authors
authors = [
    {"name": "Delia Owens"},
    {"name": "Leo Tolstoy"},
    {"name": "John Ronald Reuel Tolkien"},
    {"name": "Aldous Huxley"},
    {"name": "Colleen Hoover"},
]

author_docs = {}
for author in authors:
    result = db.authors.insert_one(author)
    author_docs[author["name"]] = result.inserted_id

# Sample books
books = [
    {
        "title": "Secrets of the Southern Wild",
        "author_id": author_docs["Delia Owens"],
        "year": 2024,
        "categories": ["Fiction", "Mystery", "Drama", "Contemporary"],
        "copies": 11,
        "ebook": True,
    },
    {
        "title": "War and Peace",
        "author_id": author_docs["Leo Tolstoy"],
        "year": 1869,
        "categories": ["Classic", "Historical", "Novel"],
        "copies": 84,
        "ebook": True,
    },
    {
        "title": "The Fellowship of the Ring",
        "author_id": author_docs["John Ronald Reuel Tolkien"],
        "year": 1954,
        "categories": ["Fantasy", "Adventure", "Epic"],
        "copies": 2,
        "ebook": False,
    },
    {
        "title": "Brave New World",
        "author_id": author_docs["Aldous Huxley"],
        "year": 1932,
        "categories": ["Dystopia", "Science Fiction", "Classic"],
        "copies": 22,
        "ebook": True,
    },
    {
        "title": "The Hobbit",
        "author_id": author_docs["John Ronald Reuel Tolkien"],
        "year": 1937,
        "categories": ["Fantasy", "Adventure", "Epic"],
        "copies": 2,
        "ebook": True,
    },
    {
        "title": "It Ends with Us",
        "author_id": author_docs["Colleen Hoover"],
        "year": 2016,
        "categories": ["Romance", "Drama", "Contemporary", "Fiction", "Emotional"],
        "copies": 24,
        "ebook": True,
    },
]

db.books.insert_many(books)
print("Sample authors and books inserted successfully!")
