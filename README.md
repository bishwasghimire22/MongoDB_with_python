# MongoDB Library Application with Python

## Overview
This project demonstrates using **MongoDB** with **Python** via the **PyMongo** library. It implements a command-line interface (CLI) application for managing a library, allowing users to manage **authors** and **books** with full CRUD operations and document relationships.

---

## Features
- **CRUD Operations** for two collections:
  - **Authors**: add, list, update, delete
  - **Books**: add, list, update, delete
- **Relationships**: Each book is linked to an author via `_id`.
- **Command-Line Interface**: Simple text-based interaction.
- **Extensible**: Easily add features like search, filtering, and statistics.

---

## Installation

1. **Clone the repository**
````
git clone https://github.com/bishwasghimire22/MongoDB_with_python.git
cd mongodb_app
````
2. **Create a virtual environment**
````
python -m venv venv
````
3. **Activate the virtual environment**
   * Windows (PowerShell):
   ````
   .\venv\Scripts\Activate.ps1
   ````
   * macOS / Linux:
   ````
   source venv/bin/activate
   ````
4. **Install dependencies**
   ````
   pip install -r requirements.txt
   ````
