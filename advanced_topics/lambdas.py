
from functools import reduce


def simple_lambda():
    """A simple lambda function"""
    print("*************** A simple lambda function ***************")

    plus_5 = lambda x: x + 5
    print(plus_5(4))

    return lambda x: x * 2


def lambda_as_parameter():
    """A lambda function as a parameter"""
    print("*************** A lambda function as a parameter ***************")

    def apply_func(x, fn):
        return fn(x)

    def add_one(x):
        return x + 1

    print(apply_func(2, add_one))
    print(apply_func(2, lambda x: x + 1))


def lambda_as_return_value():
    """A lambda function as a return value"""
    print("*************** A lambda function as a return value ***************")

    def apply_func(fn, *args, **kwargs):
        return fn(*args, **kwargs)

    print(apply_func(lambda x, y: x + y, 1, 2))
    print(apply_func(lambda x, *, y: x + y, 1, y=2))
    print(apply_func(lambda *args: sum(args), 1, 2, 3, 4))
    print(apply_func(lambda **kwargs: sum(kwargs.values()), a=1, b=2, c=3))


def lambda_in_list():
    """A lambda function in a list"""
    print("*************** A lambda function in a list ***************")

    def apply_func(fn, *args, **kwargs):
        return fn(*args, **kwargs)

    funcs = [
        lambda x: x ** 0.5,
        lambda x: 1 / x
    ]

    print(apply_func(funcs[0], 4))
    print(apply_func(funcs[1], 4))


def lambda_in_dict():
    """A lambda function in a dictionary"""
    print("*************** A lambda function in a dictionary ***************")

    def apply_func(fn, *args, **kwargs):
        return fn(*args, **kwargs)

    funcs = {
        'sqrt': lambda x: x ** 0.5,
        'square': lambda x: x ** 2
    }

    print(apply_func(funcs['sqrt'], 4))
    print(apply_func(funcs['square'], 4))


def lambda_in_class():
    """A lambda function in a class"""
    print("*************** A lambda function in a class ***************")

    class Adder:
        def __init__(self, n):
            self.n = n

        def __call__(self, x):
            return self.n + x

    plus_3 = Adder(3)
    print(plus_3(4))


def lambda_in_map():
    # Using map with a custom lambda to square each element in a list
    print("*************** Using map with a custom lambda to square each element in a list ***************")

    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(squared)  # Output: [1, 4, 9, 16, 25]


def lambda_in_filter():
    # Using filter with a custom lambda to get even numbers from a list
    print("*************** Using filter with a custom lambda to get even numbers from a list ***************")

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(evens)  # Output: [2, 4, 6, 8]


def lambda_in_sort():
    # Using sorted with a custom lambda to sort a list of tuples by the second element
    print("*************** Using sorted with a custom lambda to sort a list of tuples by the second element ***************")

    pairs = [(1, 5), (2, 3), (3, 8), (4, 1)]
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    print(sorted_pairs)  # Output: [(4, 1), (2, 3), (1, 5), (3, 8)]


def lambda_in_reduce():
    # Using reduce with a custom lambda to calculate the product of all elements in a list
    print("*************** Using reduce with a custom lambda to calculate the product of all elements in a list ***************")

    numbers = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x * y, numbers)
    print(product)  # Output: 120


def lambda_in_decorator():
    # Using a lambda function in a decorator
    print("*************** Using a lambda function in a decorator ***************")

    def logger(func):
        def inner(*args, **kwargs):
            print(f'Arguments were: {args}, {kwargs}')
            return func(*args, **kwargs)
        return inner

    @logger
    def foo1(x, y=1):
        return x * y

    @logger
    def foo2():
        return 2

    foo1(5, 4)
    foo1(1)
    foo2()


if __name__ == '__main__':
    print(simple_lambda()(5))
    lambda_as_parameter()
    lambda_as_return_value()
    lambda_in_list()
    lambda_in_dict()
    lambda_in_class()
    lambda_in_map()
    lambda_in_filter()
    lambda_in_sort()
    lambda_in_reduce()
    lambda_in_decorator()

