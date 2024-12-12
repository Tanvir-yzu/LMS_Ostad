import json
from tabulate import tabulate

def view_all_books(all_books):
    if not all_books:
        print("No Book found.")
        return

    table_data = [
        [book['title'], book['author'], book['isbn'], book['year'], book['price'], book['quantity'], book['bookAddedAt'], book['bookLastUpdatedAt']] for book in all_books
    ]
    table_headers = ["Title", "Author", "ISBN", "Year", "Price", "Quantity", "Added At", "Last Updated At"]
    print(tabulate(table_data, headers=table_headers, tablefmt="grid"))