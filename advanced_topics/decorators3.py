
import time


def retry(max_retries):
    def retry_decorator(func):
        def _wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    func(*args, **kwargs)
                except Exception:
                    time.sleep(1)
        return _wrapper
    return retry_decorator


@retry(4)
def might_fail():
    print("might_fail")
    raise Exception


if __name__ == '__main__':
    might_fail()
