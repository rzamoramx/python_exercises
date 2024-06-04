
import multiprocessing as mp
import queue

mp.set_start_method('spawn', force=True)

"""
multiprocessing is a package that supports spawning processes using an API similar to the threading module.
this is the way to by pass the GIL (Global Interpreter Lock) limitation in python.
there are two main ways to use the multiprocessing module:
- using a pool of workers
- using a queue of tasks
"""


# Worker function to do some work
def do_work(string):
    return string.upper()


# Worker function to process tasks from the queue
def worker_function(q):
    while True:
        try:
            task = q.get(timeout=1)  # Get a task from the queue with a timeout
            # Process the task here
            result = do_work(task)
            print(result)
            # q.task_done()
        except queue.Empty:
            break


"""
multiprocessing example using queue of tasks
"""

def mp_queue_of_tasks():
    # Create a queue to hold tasks
    # be careful, this queue is not the same as the queue module, on windows this causes exceptions
    task_queue = mp.Queue()

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
multiprocessing example using pool of workers
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
