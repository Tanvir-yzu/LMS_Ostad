from server import save_books
from datetime import datetime

def update_books(all_books):
    search_book = input("Enter Book Title to Update: ")
    for index, book in enumerate(all_books):
        if book["title"] == search_book:
            new_title = input("Enter new title (leave blank to keep existing): ") or book["title"]
            new_author = input("Enter new author name (leave blank to keep existing): ") or book["author"]
            while True:
                try:
                    new_year = int(input("Enter publishing year (leave blank to keep existing): ") or book["year"])
                    break
                except ValueError:
                    print("Invalid year. Please enter a number.")
            while True:
                try:
                    new_price = int(input("Enter new book price (leave blank to keep existing): ") or book["price"])
                    break
                except ValueError:
                    print("Invalid price. Please enter a number.")
            while True:
                try:
                    new_quantity = int(input("Enter new book quantity (leave blank to keep existing): ") or book["quantity"])
                    break
                except ValueError:
                    print("Invalid quantity. Please enter a number.")

            book_last_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book["title"] = new_title
            book["author"] = new_author
            book["year"] = new_year
            book["price"] = new_price
            book["quantity"] = new_quantity
            book["bookLastUpdatedAt"] = book_last_updated_at

            save_books(all_books)
            print(f"Book '{search_book}' updated successfully!")
            return all_books  

    print(f"Book '{search_book}' not found.")