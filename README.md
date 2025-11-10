# MongoDB Movie Database Application with Python

## Overview

This project demonstrates how to use **MongoDB** with **Python** via the **PyMongo** library.  
It implements a **command-line interface (CLI)** application for managing a **movie database**, allowing users to manage **directors** and **movies** with full CRUD operations and **document relationships**.

Movies store **director references (`director_id`)** instead of director names, ensuring proper **referential integrity**.

---

## Features

- **CRUD Operations** for two collections:
  - **Directors** — Add, list, update, delete
  - **Movies** — Add, list, update, delete
- **Relationships:** Each movie references a director via `_id`.
- **Cascade Delete:** Deleting a director removes all their movies automatically.
- **Director Details View:** View a director’s profile along with all their movies.
- **Command-Line Interface:** Simple, interactive terminal menu.
- **Extensible:** Easily extendable for search, filtering, or analytics features.

---

## Installation

1. Clone the repository

```
git clone https://github.com/bishwasghimire22/MongoDB_with_python.git
cd MongoDB_with_python
```

2. **Create a virtual environment**

```
python -m venv venv
```

3. **Activate the virtual environment**
   - Windows (PowerShell):
   ```
   .\venv\Scripts\Activate.ps1
   ```
   - macOS / Linux:
   ```
   source venv/bin/activate
   ```
4. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

## Quick Start - Seed Sample Data

After cloning the repository, you can populate the database with sample directors and movies:

```
python seed_data.py
```

## Default connection is to a local MongoDB instance on port 27017 only

```
mongodb://localhost:27017/
```

- **Optional:** set MONGODB_URI environment variable for remote MongoDB Atlas connection.

## Usage

Run the application:

```
python main.py

```

--- Movie Database CLI ---

1. Add Director
2. Add Movie
3. List Directors
4. List Movies
5. Update Director
6. Update Movie
7. Delete Director
8. Delete Movie
9. View Director Details
10. Exit
