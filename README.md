# MongoDB Library Application with Python

## Overview

This project demonstrates using **MongoDB** with **Python** via the **PyMongo** library.  
It implements a command-line interface (CLI) application for managing a library, allowing users to manage **authors** and **books** with full CRUD operations and **document relationships**.

Books stores **author references (`author_id`)** instead of author names, ensuring referential integrity.

---

## Features

- **CRUD Operations** for two collections:
  - **Authors**: add, list, update, delete
  - **Books**: add, list, update, delete
- **Relationships**: Each book references an author via `_id`.
- **Automatic updates**: Updating an author’s name reflects in all their books.
- **Cascade delete**: Deleting an author removes all books linked to them.
- **Command-Line Interface**: Simple text-based interaction.
- **Extensible**: Supports adding search, filtering, and statistics.

---

## Installation

1. **Clone the repository**

```
git clone https://github.com/bishwasghimire22/MongoDB_with_python.git
cd mongodb_app
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

After cloning the repository, you can populate the database with sample authors and books:

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

--- Library CLI ---

1. Add Author
2. Add Book
3. List Authors
4. List Books
5. Update Author
6. Update Book
7. Delete Author
8. Delete Book
9. Exit
   Choose an option:
