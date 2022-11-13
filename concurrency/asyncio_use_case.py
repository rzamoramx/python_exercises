
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


def process():
    global start_at
    start_at = time.time()

    # loop = asyncio.get_event_loop() deprecation since python 3.11 you need to use new_event... and set_event...
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    tasks = [
        loop.create_task(sum_numbers("A", [1,2,3])),
        loop.create_task(sum_numbers("B", [2,4,6,8,10])),
        loop.create_task(sum_numbers("C", [2,4,6,10])),
        loop.create_task(sum_numbers("D", [2,4,1,8,10])),
        loop.create_task(sum_numbers("E", [2,4,0,8,10])),
        loop.create_task(sum_numbers("F", [2,4,6])),
        loop.create_task(sum_numbers("G", [2,4,8,10])),
        loop.create_task(sum_numbers("H", [6,8,10])),
    ]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    end = time.time()
    print(f'Time: {end-start_at:.2f} sec')


if __name__ == '__main__':
    process()
