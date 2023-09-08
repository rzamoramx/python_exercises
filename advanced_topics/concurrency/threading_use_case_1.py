
import threading
import time
import random


def worker(number):
    sleep = random.randrange(1, 20)
    time.sleep(sleep)
    print("I am Worker {}, I slept for {} seconds".format(number, sleep))


def run_case_1():
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        t.start()

    print("All Threads are queued, let's see when they finish!")


def worker2():
    print("do thing 1 WORKER 2")
    print("do thing 2 WORKER 2")
    print("do thing 3 WORKER 2")


def worker3():
    print("do thing 1 WORKER 3")
    print("do thing 2 WORKER 3")
    print("do thing 3 WORKER 3")


def run_case_2():
    t1 = threading.Thread(target=worker2)
    t2 = threading.Thread(target=worker3)

    t1.start(), t2.start()

    t1.join(), t2.join()


if __name__ == '__main__':
    run_case_1()
    run_case_2()
