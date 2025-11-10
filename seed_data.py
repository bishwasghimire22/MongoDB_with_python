from pymongo import MongoClient
import os

# Use local MongoDB or environment variable
MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)

# Use the new database name
db = client["movies_db"]

# Clear existing data (optional, for testing)
# db.directors.delete_many({}) ##Uncomment to clear the directors collection
# db.movies.delete_many({})  ##Uncomment to clear the movies collection

# ----- Sample Directors -----
directors = [
    {
        "name": "Christopher Nolan",
        "birth_year": 1970,
        "nationality": "British-American",
        "awards": ["Oscar", "BAFTA"],
    },
    {
        "name": "Hayao Miyazaki",
        "birth_year": 1941,
        "nationality": "Japanese",
        "awards": ["Academy Honorary Award"],
    },
    {
        "name": "Greta Gerwig",
        "birth_year": 1983,
        "nationality": "American",
        "awards": ["Golden Globe", "BAFTA"],
    },
    {
        "name": "Denis Villeneuve",
        "birth_year": 1967,
        "nationality": "Canadian",
        "awards": ["César Award", "BAFTA"],
    },
    {
        "name": "Steven Spielberg",
        "birth_year": 1946,
        "nationality": "American",
        "awards": ["Oscar", "Golden Globe", "BAFTA"],
    },
]

# Insert directors and store their IDs
director_docs = {}
for director in directors:
    result = db.directors.insert_one(director)
    director_docs[director["name"]] = result.inserted_id

# ----- Sample Movies -----
movies = [
    {
        "title": "Inception",
        "release_year": 2010,
        "director_id": director_docs["Christopher Nolan"],
        "genres": ["Sci-Fi", "Thriller"],
        "rating": 8.8,
    },
    {
        "title": "Interstellar",
        "release_year": 2014,
        "director_id": director_docs["Christopher Nolan"],
        "genres": ["Sci-Fi", "Adventure", "Drama"],
        "rating": 8.6,
    },
    {
        "title": "Spirited Away",
        "release_year": 2001,
        "director_id": director_docs["Hayao Miyazaki"],
        "genres": ["Animation", "Fantasy"],
        "rating": 8.6,
    },
    {
        "title": "Barbie",
        "release_year": 2023,
        "director_id": director_docs["Greta Gerwig"],
        "genres": ["Comedy", "Fantasy", "Adventure"],
        "rating": 7.0,
    },
    {
        "title": "Dune: Part One",
        "release_year": 2021,
        "director_id": director_docs["Denis Villeneuve"],
        "genres": ["Sci-Fi", "Adventure"],
        "rating": 8.1,
    },
    {
        "title": "E.T. the Extra-Terrestrial",
        "release_year": 1982,
        "director_id": director_docs["Steven Spielberg"],
        "genres": ["Family", "Sci-Fi", "Adventure"],
        "rating": 7.8,
    },
]

# Insert movies
db.movies.insert_many(movies)
print("Sample directors and movies inserted successfully!")
