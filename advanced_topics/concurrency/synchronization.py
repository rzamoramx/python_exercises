import threading
import time

"""
Synchronization is the process of coordinating the access of multiple threads to shared data. This is necessary to 
prevent race conditions and data corruption. 
Synchronization is a technique that can be used to achieve thread safety. However, there are other ways to achieve 
thread safety, such as using immutable objects or designing your code in a way that avoids data races. And we can
grouped locks and semaphores as synchronization topic:
    Locks: In Python, you can use the threading.Lock or multiprocessing.Lock classes to create locks that protect 
        critical sections of code. Locks are a synchronization mechanism used to ensure that only one thread or process 
        can access a particular resource at a time.
    Semaphores: Python provides the threading.Semaphore and multiprocessing.Semaphore classes, which are used for 
        controlling access to a resource with a limited number of available "slots." Semaphores can be used for more 
        complex synchronization scenarios beyond simple locking.
"""

# create a lock
lock = threading.Lock()

# create a semaphore that can be accessed by 3 threads at a time
semaphore = threading.Semaphore(3)

# shared resource
counter = 0


# ++++++++++++++++++++++++++++++++++++++ Lock technique +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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


def lock_thread_safety():
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


# ++++++++++++++++++++++++++++++++++++++ Semaphore technique +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def worker(worker_id):
    print(f'worker {worker_id} is waiting to access a semaphore')

    # acquire semaphore
    semaphore.acquire()
    print(f'worker {worker_id} has acquired a semaphore')

    # Simulate som work
    for i in range(2):
        time.sleep(1)
        print(f'worker {worker_id} is working')

    # release semaphore
    semaphore.release()
    print(f'worker {worker_id} has released a semaphore')


def semaphore_thread_safety():
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    # wait for all threads to finish
    for t in threads:
        t.join()

    print('all workers have finished')


if __name__ == '__main__':
    print("=============lOCK====================")
    lock_thread_safety()
    print("=====================================")
    print("=============SEMAPHORE===============")
    semaphore_thread_safety()
    print("=====================================")