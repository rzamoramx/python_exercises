
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


def example1():
    global start_at
    start_at = time.time()

    tasks = [
        cpu_high("A", 123456789000),
        cpu_high("B", 12345000),
        cpu_high("C", 34547890000),
        cpu_high("D", 100000000000),
        cpu_high("E", 23234000),
        cpu_high("F", 123000),
        cpu_high("G", 897874000),
        cpu_high("H", 9872343000),
    ]

    end = time.time()
    print(f'Time: {end-start_at:.2f} sec')


def example2():
    global start_at
    start_at = time.time()

    tasks = [
        sum_numbers("A", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        sum_numbers("B", [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
        sum_numbers("C", [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),
        sum_numbers("D", [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]),
        sum_numbers("E", [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),
    ]

    end = time.time()
    print(f'Time: {end-start_at:.2f} sec')


if __name__ == '__main__':
    example1()
    example2()
