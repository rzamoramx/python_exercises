
import functools


def simple_decorator(func):
    """
    the wraps decorator is for preserving info (like __name__, __doc__)
     of the function caller
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call', args, kwargs)
        values = func(*args, **kwargs)
        print('values', values)
        return values * 2
    return wrapper


@simple_decorator
def use_simple_decorator(number):
    number += 1
    return number


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        print('call', args, kwargs)
        values = func(*args, **kwargs)
        print('values', values)
        return values.upper()
    return wrapper_do_twice


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


if __name__ == '__main__':
    print(use_simple_decorator(2))
    print("-"*30)

    print(return_greeting("Rod"))
    print("-"*30)