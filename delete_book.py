from server import save_books

def delete_books(all_books):
    search_book = input("Enter Book Title to Delete: ")
    for book in all_books:
        if book["title"] == search_book:
            all_books.remove(book)
            try:
                save_books(all_books)
                print(f"Book '{search_book}' deleted successfully.")
            except Exception as e:
                print(f"Error saving changes: {e}")
                # Consider rolling back the deletion or notifying the user
            return all_books

    print(f"Book '{search_book}' not found.")