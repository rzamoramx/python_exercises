
from book_type import Book


# for simplicity de data is hardcoded, but it real scenarios it will be fetched from a database
def get_books(author: str = None):
    books = [
        Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
        ),
        Book(
            title="The DaVinci Code",
            author="Dan Brown",
        ),
        Book(
            title="Angels & Demons",
            author="Dan Brown",
        ),
    ]

    if author:
        return [book for book in books if book.author == author]
    return books
