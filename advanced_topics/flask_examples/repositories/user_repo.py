

users = {
    'Ivancito': {'username': 'Ivancito', 'password': '1234'},
    'user2': {'username': 'user2', 'password': 'password2'},
}


def get_user(username):
    return users.get(username)
