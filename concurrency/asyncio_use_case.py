
import time
import asyncio


start_at = 0


async def sleep():
    print(f'Time: {time.time() - start_at:.2f}')
    # time.sleep(1) this wrong use, block truly concurrency
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


def process():
    # Asyncio is affected by GIL and in some cases is worse than a single thread
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


if __name__ == '__main__':
    process()
