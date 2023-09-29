import threading
import queue

# create a shared queue
queue = queue.Queue()


# function to put data in the queue
def producer():
    for i in range(5):
        queue.put(i)
        print(f'Produced: {i}')


# function to get data from the queue
def consumer():
    while True:
        data = queue.get()
        if data is None:
            break
        print(f'Consumed: {data}')
        queue.task_done()


def run_syncro_comm():
    # create producer and consumer threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    # start threads
    producer_thread.start()
    consumer_thread.start()

    # wait for the producer to finish
    producer_thread.join()

    # signal the consumer to exit
    queue.put(None)

    # wait for the consumer to finish
    consumer_thread.join()


if __name__ == '__main__':
    run_syncro_comm()
