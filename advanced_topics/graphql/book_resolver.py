
from advanced_topics.graphql.user_schema import schema as user


# for simplicity de data is hardcoded, but it real scenarios it will be fetched from a database
def get_books():
    return [
        Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
        ),
    ]