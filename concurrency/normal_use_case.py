
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


def process():
    global start_at
    start_at = time.time()

    tasks = [
        cpu_high("A", 123456789),
        cpu_high("B", 12345),
        cpu_high("C", 34547890),
        cpu_high("D", 100000000),
        cpu_high("E", 23234),
        cpu_high("F", 123),
        cpu_high("G", 897874),
        cpu_high("H", 9872343),
    ]

    end = time.time()
    print(f'Time: {end-start_at:.2f} sec')


if __name__ == '__main__':
    process()
