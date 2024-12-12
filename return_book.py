from server import save_books, save_lend_records

def return_book(books, lend_records):
    title = input("Enter book title: ")
    borrower_name = input("Enter borrower's name: ")

    for record in lend_records:
        if record['title'] == title and record['borrower_name'] == borrower_name:
            lend_records.remove(record)
            for book in books:
                if book['title'] == title:
                    book['quantity'] += 1
                    try:
                        save_books(books)
                        save_lend_records(lend_records)
                        print(f"Book '{title}' returned by {borrower_name}.")
                    except Exception as e:
                        print(f"Error saving changes: {e}")
                    return
            else:
                print("Book not found in library.")
            break  
    else:
        print("Borrower not found for this book.")