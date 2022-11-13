
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


def run():
    global start_at
    start_at = time.time()
    tasks = [
        ("A", [1,2,3]),
        ("B", [2,4,6,8,10]),
        ("C", [2,4,6,10]),
        ("D", [2,4,1,8,10]),
        ("E", [2,4,0,8,10]),
        ("F", [2,4,6]),
        ("G", [2,4,8,10]),
        ("H", [6,8,10]),
    ]

    procs = []
    for task in tasks:
        # print(name)
        proc = Process(target=sum_numbers, args=task)
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()

    end = time.time()
    print(f'Time: {end-start_at:.2f} sec')


if __name__ == '__main__':
    run()
