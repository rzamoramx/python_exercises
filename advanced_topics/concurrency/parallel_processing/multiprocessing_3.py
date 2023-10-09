import time
import multiprocessing


def countdown(number):
    while number > 0:
        number -=1


def test_mp():
    start = time.time()

    count = 100000000

    t1 = multiprocessing.Process(target=countdown, args=(count,))
    t2 = multiprocessing.Process(target=countdown, args=(count,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f'Time enlapsed {time.time() - start }')


if __name__ == '__main__':
    test_mp()
