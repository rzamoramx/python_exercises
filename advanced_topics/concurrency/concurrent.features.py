
import concurrent.futures
import multiprocessing

"""
concurrent.futures is a high-level interface for asynchronously executing callables. It provides a high-level
interface for asynchronously executing callables. The asynchronous execution can be performed with threads, using
ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is
defined by the abstract Executor class.
"""


# Function to simulate some task
def process_data(data):
    res = data * 2
    return res


def calculate_square(n):
    return n ** 2


data_to_process = [1, 2, 3, 4, 5]


# Using ThreadPoolExecutor
# Note: consider implications of GIL
def thread_pool_executor():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for processing
        future_to_data = {executor.submit(process_data, data): data for data in data_to_process}

        # Retrieve results as they complete
        for future in concurrent.futures.as_completed(future_to_data):
            data = future_to_data[future]
            try:
                result = future.result()
                print(f"Processed {data} -> Result: {result}")
            except Exception as e:
                print(f"Error processing {data}: {e}")


# Using ProcessPoolExecutor
# Note: here GIL is not a concern
def process_pool_executor():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Submit tasks for processing
        results = executor.map(calculate_square, data_to_process)

        # Retrieve and print results
        for number, result in zip(data_to_process, results):
            print(f"Square of {number} is {result}")


# Using ProcessPoolExecutor with max workers
def process_pool_executor_max_workers():
    # Get the number of CPUs
    cpu_count = multiprocessing.cpu_count() - 2
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count) as executor:
        # Submit tasks for processing
        results = executor.map(calculate_square, data_to_process)

        # Retrieve and print results
        for number, result in zip(data_to_process, results):
            print(f"Square of {number} is {result}")


if __name__ == '__main__':
    thread_pool_executor()
    print("--"*20)

    process_pool_executor()
    print("--"*20)

    process_pool_executor_max_workers()
