
from contextlib import contextmanager


# class as custom manager
class CustomContextManager(object):
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print('entering...')
        return f"hello from class, {self.name}"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting context manager...')
        # handling errors
        if isinstance(exc_val, IndexError):
            print(f'exception: {exc_val} --> {exc_tb}')
            return True


# function as context manager, using generators
@contextmanager
def greeting_cm(name: str):
    print('entering func as context manager')
    yield f"hello from func, {name}"
    print('exiting context manager')


if __name__ == '__main__':
    with greeting_cm("Rod") as greet:
        print(greet)

    print('-'*30)

    with CustomContextManager(name="Rod") as greeting:
        print(greeting)
        greeting[100]
