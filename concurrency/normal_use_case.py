
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


def process():
    global start_at
    start_at = time.time()
    tasks = [
        sum_numbers("A", [1,2,3]),
        sum_numbers("B", [2,4,6,8,10]),
        sum_numbers("C", [2,4,6,10]),
        sum_numbers("D", [2,4,1,8,10]),
        sum_numbers("E", [2,4,0,8,10]),
        sum_numbers("F", [2,4,6]),
        sum_numbers("G", [2,4,8,10]),
        sum_numbers("H", [6,8,10]),
    ]
    end = time.time()
    print(f'Time: {end-start_at:.2f} sec')


if __name__ == '__main__':
    process()
