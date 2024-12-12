from server import save_books
import random
from datetime import datetime

def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    year = int(input("Enter Publishing Year Number: "))
    price = int(input("Enter Book Price: "))

    while True:
        try:
            quantity = int(input("Enter Quantity Number: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid quantity. Please enter a whole number (integer).")

    isbn = random.randint(10000, 99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
        "bookAddedAt": bookAddedAt,
        "bookLastUpdatedAt": ""
    }

    all_books.append(book)

    try:
        save_books(all_books)
        print("Books Added Successfully")
    except Exception as e:
        print(f"Error saving books: {e}")

    return all_books