import threading
import queue

"""
Thread safety is the property of a program or object that can be safely accessed by multiple threads simultaneously. 
And Queue, Priority Queue, and LIFO can be grouped as thread-safe topic:
    Queue: The queue.Queue class in Python is a thread-safe data structure that provides a synchronized queue for 
        inter-thread communication. It's often used for passing data between threads safely.
    PriorityQueue: The queue.PriorityQueue is another thread-safe queue that allows you to prioritize elements based 
        on a specified key.
    LifoQueue: The queue.LifoQueue is a thread-safe Last-In-First-Out (LIFO) queue.
"""

q = queue.Queue()
pq = queue.PriorityQueue()
lq = queue.LifoQueue()


# ++++++++++++++++++++++++++++++++++++++ Queue ++++++++++++++++++++++++++++++++++++++++++++++++++++++
def producer(q):
    for i in range(5):
        q.put(i)
        print(f"Produced: {i}")


def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        q.task_done()


def queue_thread_safety():
    producer_thread = threading.Thread(target=producer, args=(q,))
    consumer_thread = threading.Thread(target=consumer, args=(q,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    q.put(None)  # Signal the consumer to exit
    consumer_thread.join()


# ++++++++++++++++++++++++++++++++++++++ Priority Queue ++++++++++++++++++++++++++++++++++++++++++++++++++++++

def pq_producer(pq):
    pq.put((2, "High Priority Task"))
    pq.put((1, "Highest Priority Task"))
    pq.put((3, "Low Priority Task"))
    pq.put((1, "Another Highest Priority Task"))


def pq_consumer(pq):
    while True:
        item = pq.get()
        if item is None:
            pq.task_done()
            break
        print(f"PQ Consumed: {item[1]}")
        pq.task_done()


def priority_queue_thread_safety():
    producer_thread = threading.Thread(target=pq_producer, args=(pq,))
    consumer_thread = threading.Thread(target=pq_consumer, args=(pq,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    pq.put(None)  # Signal the consumer to exit
    consumer_thread.join()


# ++++++++++++++++++++++++++++++++++++++ LIFO Queue ++++++++++++++++++++++++++++++++++++++++++++++++++++++

def lq_producer(lq):
    for i in range(5):
        lq.put(i)
        print(f"LQ Pushed: {i}")


def lq_consumer(lq):
    while True:
        item = lq.get()
        if item is None:
            break
        print(f"LQ Popped: {item}")
        lq.task_done()


def lifo_queue_thread_safety():
    producer_thread = threading.Thread(target=lq_producer, args=(q,))
    consumer_thread = threading.Thread(target=lq_consumer, args=(q, ))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    lq.put(None)  # Signal the consumer to exit
    consumer_thread.join()


if __name__ == '__main__':
    print("=============QUEUE===================")
    queue_thread_safety()
    print("=====================================")
    print("=============PRIORITY QUEUE==========")
    priority_queue_thread_safety()
    print("=====================================")
    print("=============LIFO QUEUE==============")
    lifo_queue_thread_safety()
    print("=====================================")


