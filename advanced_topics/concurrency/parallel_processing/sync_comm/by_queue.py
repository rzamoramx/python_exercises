
import multiprocessing

"""
In multiprocessing, when we want to communicate between processes, we can use a queue.
This is a simple example of how to use it.
"""


def calculate_partial_sum(start, end, result_queue):
    partial_sum = sum(range(start, end))
    result_queue.put(partial_sum)


if __name__ == "__main__":
    num_processes = 4
    result_queue = multiprocessing.Queue()
    processes = []

    # Define ranges for each process
    ranges = [(1, 25001), (25001, 50001), (50001, 75001), (75001, 100001)]

    for i in range(num_processes):
        start, end = ranges[i]
        process = multiprocessing.Process(target=calculate_partial_sum, args=(start, end, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_sum = 0
    for _ in range(num_processes):
        partial_sum = result_queue.get()
        total_sum += partial_sum
        print(f"Partial Sum: {partial_sum}")

    print(f"Total Sum: {total_sum}")

