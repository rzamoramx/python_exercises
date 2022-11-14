
from multiprocessing import Process
import time


start_at = 0


def sleep():
    print(f'Time: {time.time() - start_at:.2f}')
    time.sleep(1)


def sum_numbers(task_name: str, numbers: [int]):
    total = 0
    for number in numbers:
        print(f'Task name: {task_name}: ... total: {total} and number: {number}')
        sleep()
        total += number
    print(f'Task name: {task_name}: sum = {total}\n')


def cpu_high(task_name: str, count: int):
    print(f'entering task: {task_name}...')
    for x in range(count):
        x*x
    print(f'finish task: {task_name}')


def run():
    # Multiprocessing is true concurrency cause every task is launched in an isolated python interpreter, so GIL
    # is bypassed this way.
    global start_at
    start_at = time.time()
    tasks = [
        ("A", 123456789),
        ("B", 12345),
        ("C", 34547890),
        ("D", 100000000),
        ("E", 23234),
        ("F", 123),
        ("G", 897874),
        ("H", 9872343),
    ]

    procs = []
    for task in tasks:
        # print(name)
        proc = Process(target=cpu_high, args=task)
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()

    end = time.time()
    print(f'Time: {end-start_at:.2f} sec')


if __name__ == '__main__':
    run()
