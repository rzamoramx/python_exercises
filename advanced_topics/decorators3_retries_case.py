
import time
from functools import wraps


def retry(arg):
    """
    with a wrapper itself we can pass params to decorator
    """
    def retry_decorator(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    func(*args, **kwargs)
                except Exception:
                    time.sleep(1)
        return _wrapper
    if callable(arg):
        max_retries = 2
        return retry_decorator(arg)
    else:
        max_retries = arg
        return retry_decorator


@retry(4)
def might_fail_with_max_four_tries():
    print("might fail and retries max 4 times")
    raise Exception


@retry
def might_fail_with_default_max_retries():
    print("might fail and retries max 2 times")
    raise Exception


if __name__ == '__main__':
    might_fail_with_max_four_tries()
    might_fail_with_default_max_retries()

