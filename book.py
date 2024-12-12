from server import load_books, load_lend_records
from lend_book import lend_book
from return_book import return_book
import add_book
import view_all_books
import update_book
import delete_book

def main():
    books = load_books()
    lend_records = load_lend_records()

    while True:
        print("\nWelcome to Library Management System")
        print("0. Exit")
        print("1. Add Books")
        print("2. View All Books")
        print("3. Book Update")
        print("4. Book Remove/Delete")
        print("5. Lend Book")
        print("6. Return Book")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Thanks for using Library Management System ")
            break
        elif choice == 1:
            books = add_book.add_books(books)
        elif choice == 2:
            view_all_books.view_all_books(books)
        elif choice == 3:
            update_book.update_books(books)
        elif choice == 4:
            delete_book.delete_books(books)
        elif choice == 5:
            lend_book(books, lend_records)  
        elif choice == 6:
            return_book(books, lend_records)  
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()