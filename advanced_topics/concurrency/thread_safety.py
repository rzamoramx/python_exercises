import threading

# create a lock
lock = threading.Lock()

# shared resource
counter = 0


# function to increment counter in a thread-safe way
def increment_counter():
    global counter
    """lock.acquire()
    try:
        counter += 1
    finally:
        lock.release()"""
    with lock:
        counter += 1


def run_thread_safety():
    print(f'Counter value: {counter}')

    # create multiple threads
    threads = []
    for _ in range(5):
        t = threading.Thread(target=increment_counter)
        threads.append(t)

    # start threads
    for t in threads:
        t.start()

    # wait for threads to finish
    for t in threads:
        t.join()

    print(f'Counter value: {counter}')


if __name__ == '__main__':
    run_thread_safety()

