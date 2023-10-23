
import requests


def perform_simple_query():
    # Define the GraphQL query
    query = '''
    {
      books {
        title
        author
      }
    }
    '''

    # Set the GraphQL server URL
    url = 'http://localhost:8000/book'

    # Set the headers for the HTTP POST request
    headers = {
        'Content-Type': 'application/json',
    }

    # Create a dictionary representing the GraphQL request
    data = {
        'query': query,
    }

    # Send the GraphQL query as a POST request
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        result = response.json()
        print("Data received:")
        print(result['data'])
    else:
        print("Request failed with status code:", response.status_code)
        print(response.text)


def filter_query():
    # Define your GraphQL query
    query = """
    query {
        books(author: "Dan Brown") {
            title
            author
        }
    }
    """

    # Send the query to the GraphQL endpoint
    url = "http://localhost:8000/book"  # Change the URL to match your server
    response = requests.post(url, json={"query": query})

    # Check the response and print the filtered books
    print("Books filtered by author:")
    if response.status_code == 200:
        data = response.json()
        books = data["data"]["books"]
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}")
    else:
        print(f"Failed to fetch books. Status code: {response.status_code}")


if __name__ == '__main__':
    perform_simple_query()
    filter_query()
