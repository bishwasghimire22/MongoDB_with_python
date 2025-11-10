from bson.objectid import ObjectId
from database import db


# ---------- CREATE ----------
def add_director():
    name = input("Director name: ")
    if db.directors.find_one({"name": name}):
        print(f"Director '{name}' already exists.")
        return

    birth_year = int(input("Birth year: "))
    nationality = input("Nationality: ")
    awards = input("Awards (comma-separated): ").split(",")

    director = {
        "name": name,
        "birth_year": birth_year,
        "nationality": nationality,
        "awards": [a.strip() for a in awards if a.strip()],
    }

    db.directors.insert_one(director)
    print(f"Director '{name}' added successfully!")


def add_movie():
    title = input("Movie title: ")
    if db.movies.find_one({"title": title}):
        print(f"Movie '{title}' already exists.")
        return

    director_name = input("Director name: ")
    director = db.directors.find_one({"name": director_name})
    if not director:
        print(f"Director '{director_name}' not found. Add the director first.")
        return

    release_year = int(input("Release year: "))
    genres = input("Genres (comma-separated): ").split(",")
    rating = float(input("Rating (0–10): "))

    movie = {
        "title": title,
        "director_id": director["_id"],
        "release_year": release_year,
        "genres": [g.strip() for g in genres if g.strip()],
        "rating": rating,
    }

    db.movies.insert_one(movie)
    print(f"Movie '{title}' added successfully!")


# ---------- READ ----------
def list_directors():
    print("\nDirectors:")
    for director in db.directors.find():
        print(
            f"- {director['name']} ({director['birth_year']}, {director['nationality']})"
        )
        if director.get("awards"):
            print(f"  Awards: {', '.join(director['awards'])}")
        print()


def list_movies():
    print("\nMovies:")
    for movie in db.movies.find():
        director = db.directors.find_one({"_id": movie["director_id"]})
        director_name = director["name"] if director else "Unknown"
        print(f"- {movie['title']} by {director_name} ({movie['release_year']})")
        print(f"  Genres: {', '.join(movie['genres'])}")
        print(f"  Rating: {movie['rating']}\n")


# ---------- UPDATE ----------
def update_director():
    name = input("Director name to update: ")
    director = db.directors.find_one({"name": name})
    if not director:
        print(f"Director '{name}' not found.")
        return

    new_name = input(f"New name ({director['name']}): ") or director["name"]
    birth_year = (
        input(f"New birth year ({director['birth_year']}): ") or director["birth_year"]
    )
    nationality = (
        input(f"New nationality ({director['nationality']}): ")
        or director["nationality"]
    )
    awards = input(f"New awards (comma-separated) ({', '.join(director['awards'])}): ")

    updated_fields = {
        "name": new_name,
        "birth_year": int(birth_year),
        "nationality": nationality,
        "awards": (
            [a.strip() for a in awards.split(",")] if awards else director["awards"]
        ),
    }

    db.directors.update_one({"_id": director["_id"]}, {"$set": updated_fields})
    print(f"Director '{name}' updated successfully.")


def update_movie():
    title = input("Movie title to update: ")
    movie = db.movies.find_one({"title": title})
    if not movie:
        print(f"Movie '{title}' not found.")
        return

    new_title = input(f"New title ({movie['title']}): ") or movie["title"]

    director_name = input("New director name (leave blank to keep current): ")
    if director_name:
        director = db.directors.find_one({"name": director_name})
        if not director:
            print(f"Director '{director_name}' not found.")
            return
        director_id = director["_id"]
    else:
        director_id = movie["director_id"]

    release_year = (
        input(f"New release year ({movie['release_year']}): ") or movie["release_year"]
    )
    genres = input(f"New genres (comma-separated) ({', '.join(movie['genres'])}): ")
    rating = input(f"New rating ({movie['rating']}): ") or movie["rating"]

    updated_movie = {
        "title": new_title,
        "director_id": director_id,
        "release_year": int(release_year),
        "genres": (
            [g.strip() for g in genres.split(",")] if genres else movie["genres"]
        ),
        "rating": float(rating),
    }

    db.movies.update_one({"_id": movie["_id"]}, {"$set": updated_movie})
    print(f"Movie '{title}' updated successfully.")


# ---------- DELETE ----------
def delete_director():
    name = input("Director name to delete: ")
    director = db.directors.find_one({"name": name})
    if not director:
        print(f"Director '{name}' not found.")
        return
    db.movies.delete_many({"director_id": director["_id"]})
    db.directors.delete_one({"_id": director["_id"]})
    print(f"Director '{name}' and all their movies deleted.")


def delete_movie():
    title = input("Movie title to delete: ")
    movie = db.movies.find_one({"title": title})
    if not movie:
        print(f"Movie '{title}' not found.")
        return
    db.movies.delete_one({"_id": movie["_id"]})
    print(f"Movie '{title}' deleted successfully.")


# ----SHOW DIRECTOR DETAILS -----


def view_director_details():
    name = input("Enter director name: ")
    director = db.directors.find_one({"name": name})
    if not director:
        print(f"Director '{name}' not found.")
        return

    print(f"\n {director['name']}")
    print(f"Born: {director['birth_year']} | Nationality: {director['nationality']}")
    if director.get("awards"):
        print(f"Awards: {', '.join(director['awards'])}")

    # Fetch movies directed by this person
    movies = list(db.movies.find({"director_id": director["_id"]}))

    if not movies:
        print("No movies found for this director.\n")
        return

    print("\nMovies:")
    for m in movies:
        print(f"  - {m['title']} ({m['release_year']})")
        print(f"    Genres: {', '.join(m['genres'])}")
        print(f"    Rating: {m['rating']}")
    print()
