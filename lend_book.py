import datetime
from server import save_books, save_lend_records

def lend_book(books, lend_records):
    title = input("Enter book title: ")
    borrower_name = input("Enter borrower's name: ")

    while True:
        try:
            borrower_phone = int(input("Enter borrower's phone number: "))
            break
        except ValueError:
            print("Invalid phone number. Please enter a valid integer.")

    for book in books:
        if book['title'] == title:
            if book['quantity'] > 0:
                book['quantity'] -= 1
                lend_records.append({
                    "title": title,
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "due_date": (datetime.datetime.now() + datetime.timedelta(days=14)).strftime("%Y-%m-%d")
                })
                try:
                    save_books(books)
                    save_lend_records(lend_records)
                    print(f"Book '{title}' lent to {borrower_name}. Due date: {lend_records[-1]['due_date']}")
                except Exception as e:
                    print(f"Error saving data: {e}")
                    # Consider rolling back the changes or notifying the user
                return
            else:
                print("Not enough copies of this book available to lend.")
                return
    print(f"The book titled '{title}' is not found in the library.")
    return