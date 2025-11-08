from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")

client = MongoClient(MONGO_URI)
# Change "library" to match the name of your database
db = client["library"]
# Change the collection name to match the name of your collection
books = db.books.find()
