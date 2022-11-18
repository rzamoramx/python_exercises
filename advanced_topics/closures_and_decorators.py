
import functools


def local_func():
    def inner():
        print('inner')
    return inner


def closure(x):
    def inner(y):
        return x+y
    return inner


def simple_decorator(func):
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
    lf = local_func()
    lf()
    print("-"*30)

    add_numbers = closure(1)
    print(add_numbers(4))
    print("-"*30)

    print(use_simple_decorator(2))
    print("-"*30)

    print(return_greeting("Rod"))
    print("-"*30)
