
import typing
import strawberry
from book_type import Book
from book_resolver import get_books


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)


book_schema = strawberry.Schema(query=Query)
