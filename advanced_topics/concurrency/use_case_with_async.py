
import time
import asyncio

"""
Asyncio is a library to write concurrent code using the async/await syntax. Async uses an event loop approach.
Asyncio is suitable for IO operations, network request, DB queries, but not for CPU operations, because of the GIL 
(Global Interpreter Lock) that python has, this means that only one thread can run at a time (access to the interpreter)
, so if you have a lot of CPU operations, you will not see any improvement.
"""


start_at = 0


async def sleep():
    print(f'Time: {time.time() - start_at:.2f}')
    # time.sleep(1) this will block the event loop
    await asyncio.sleep(1)


async def sum_numbers(task_name: str, numbers: [int]):
    total = 0
    for number in numbers:
        print(f'Task name: {task_name}: ... total: {total} and number: {number}')
        await sleep()
        total += number
    print(f'Task name: {task_name}: sum = {total}\n')


async def cpu_high(task_name: str, count: int):
    print(f'entering task: {task_name}...')
    for x in range(count):
        x*x
    print(f'finish task: {task_name}')


def example1():
    # Asyncio is affected by GIL and in some cases is worse than a single thread, take care with this
    # Not all cases are good for asyncio, for example, if you have a lot of IO operations, asyncio is a good option
    # but if you have a lot of CPU operations, asyncio is not a good option
    global start_at
    start_at = time.time()

    # loop = asyncio.get_event_loop() deprecation since python 3.11 you need to use new_event... and set_event...
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    tasks = [
        loop.create_task(cpu_high("A", 123456789)),
        loop.create_task(cpu_high("B", 12345)),
        loop.create_task(cpu_high("C", 34547890)),
        loop.create_task(cpu_high("D", 100000000)),
        loop.create_task(cpu_high("E", 23234)),
        loop.create_task(cpu_high("F", 123)),
        loop.create_task(cpu_high("G", 897874)),
        loop.create_task(cpu_high("H", 9872343)),
    ]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    end = time.time()
    print(f'Time: {end-start_at:.2f} sec')


def example2():
    global start_at
    start_at = time.time()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    tasks = [
        loop.create_task(sum_numbers("A", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
        loop.create_task(sum_numbers("B", [11, 12, 13, 14, 15, 16, 17, 18, 19, 20])),
        loop.create_task(sum_numbers("C", [21, 22, 23, 24, 25, 26, 27, 28, 29, 30])),
        loop.create_task(sum_numbers("D", [31, 32, 33, 34, 35, 36, 37, 38, 39, 40])),
        loop.create_task(sum_numbers("E", [41, 42, 43, 44, 45, 46, 47, 48, 49, 50])),
    ]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    end = time.time()
    print(f'Time: {end-start_at:.2f} sec')


if __name__ == '__main__':
    example1()
    example2()
