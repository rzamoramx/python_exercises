
import time
from functools import wraps
from typing import Callable

counter = 1


def retry(arg):
    """
    with a wrapper itself we can pass params to decorator
    """
    def retry_decorator(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            for i in range(max_retries):
                try:
                    func(*args, **kwargs)
                    break
                except Exception as ex:
                    time.sleep(1)
                    if i == (max_retries - 1):
                        raise ex
        return _wrapper
    if callable(arg):
        max_retries = 2
        return retry_decorator(arg)
    else:
        max_retries = arg
        return retry_decorator


def retry_with_params(max_retries: int):
    def retry_decorator(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    func(*args, **kwargs)
                except Exception:
                    time.sleep(1)
        return _wrapper
    return retry_decorator


@retry(4)
def might_fail_with_max_four_tries():
    global counter
    print("do some thing")
    if counter < 3:
        counter += 1
        print('but... it fail')
        raise Exception
    print('all going ok :)')


@retry
def might_fail_with_default_max_retries():
    print("might fail and retries max 2 times")
    raise Exception


@retry_with_params(2)
def might_fail_with_params(param):
    print(f"might fail and retries max 2 times and param: {param}")
    raise Exception


if __name__ == '__main__':
    try:
        might_fail_with_max_four_tries()
    except Exception as e:
        print('retires exceeded')

    might_fail_with_default_max_retries()
