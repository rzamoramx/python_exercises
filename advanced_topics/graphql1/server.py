
from book_schema import book_schema
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from user_schema import user_schema


book_graphql_app = GraphQL(book_schema)
user_graphql_app = GraphQL(user_schema)

app = FastAPI()

# routes
app.add_route("/book", book_graphql_app)
app.add_websocket_route("/book", book_graphql_app)

app.add_route("/user", user_graphql_app)
app.add_websocket_route("/user", user_graphql_app)

