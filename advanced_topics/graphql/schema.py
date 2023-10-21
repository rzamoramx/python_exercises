
import strawberry
from advanced_topics.graphql.book_schema import Query as BookQuery


book_server = strawberry.Schema(query=BookQuery)