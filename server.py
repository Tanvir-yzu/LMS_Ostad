import json


def load_books():
    try:
        with open("books.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Create empty books.json file with an empty list
        with open("books.json", "w") as f:
            json.dump([], f)
        return []

def save_books(books):
    with open("books.json", "w") as f:
        json.dump(books, f, indent=4)

def load_lend_records():
    try:
        with open("lend_records.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Create empty lend_records.json file with an empty list
        with open("lend_records.json", "w") as f:
            json.dump([], f)
        return []

def save_lend_records(records):
    with open("lend_records.json", "w") as f:
        json.dump(records, f, indent=4)