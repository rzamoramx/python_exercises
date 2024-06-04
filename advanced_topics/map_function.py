
"""
map function takes a function (lambda works too) and apply that function to every element in iterable like
tuples, lists, dict
"""


def simple_example():
    numbers = [1, 2, 3, 4]
    print(list(map(add, numbers)))


def lambda_example():
    numbers = (2, 4, 6, 8)
    print(list(map(lambda x: x+x, numbers)))


def dict_example():
    dict1 = {"foo": "bar", "bla": 123}
    print(list(map(lambda prop: f'prop_name: {prop}', dict1)))


def add(n):
    return n + n


if __name__ == '__main__':
    simple_example()
    print('-'*40)
    lambda_example()
    print('-'*40)
    dict_example()
