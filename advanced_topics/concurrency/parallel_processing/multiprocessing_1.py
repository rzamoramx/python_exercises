
import multiprocessing as mp
import queue

"""
multiprocessing is a package that supports spawning processes using an API similar to the threading module.
this is the way to by pass the GIL (Global Interpreter Lock) limitation in python.
there are two main ways to use the multiprocessing module:
- using a pool of workers
- using a queue of tasks
"""


# Worker function to do some work
def do_work(task):
    print(f"Processing {task}")
    return task.upper()


# Worker function to process tasks from the queue
def worker_function(queue):
    while True:
        try:
            task = queue.get(timeout=1)  # Get a task from the queue with a timeout
            # Process the task here
            result = do_work(task)
            queue.task_done()
        except queue.Empty:
            break


"""
multiprocessing example using queue of tasks
"""

def mp_queue_of_tasks():
    # Create a queue to hold tasks
    task_queue = queue()

    # Add tasks to the queue
    task_queue.put("foo")
    task_queue.put("bar")
    task_queue.put("dummy")

    num_workers = 5
    processes = []
    for _ in range(num_workers):
        process = mp.Process(target=worker_function, args=(task_queue,))
        processes.append(process)
        process.start()

    # Wait for all worker processes to finish
    for process in processes:
        process.join()

"""
end of multiprocessing example using queue of tasks
"""

"""
multiprocessin example using pool of workers
"""

def mp_pool_of_workers():
    tasks = ["foo", "bar", "dummy"]
    with mp.Pool(processes=mp.cpu_count()) as pool:
        results = pool.map(do_work, tasks)
    print(results)

"""
end of multiprocessing example using pool of workers
"""


if __name__ == "__main__":
    mp_queue_of_tasks()
    mp_pool_of_workers()
