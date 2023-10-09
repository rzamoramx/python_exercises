
import multiprocessing as mp
import os

"""
in multiprocessing for pools usage there are apple, apply_async, map, map_async, starmap, starmap_async methods, next we will see an example of each one
"""

def square(x):
    print(f'process id: {os.getpid()}')
    return x * x

def apply():
    """
    This method is used to apply a function to a single set of arguments.
    It blocks until the result is ready.
    Suitable for cases where you want to parallelize the execution of a function with different input values and wait for each result before proceeding.
    """
    with mp.Pool(processes=4) as pool:
        result = pool.apply(square, args=(2,))
        print(result)


def apply_async():
    """
    apply_async is similar to apply but it is non-blocking
    you canuse a callback function to get the result
    Suitable for cases where you want to start multiple tasks concurrently and collect their results asynchronously.
    """
    with mp.Pool(processes=4) as pool:
        result = pool.apply_async(square, args=(2,), callback=lambda x: print(x))
        print(result.get())


def map():
    """
    map, this method applies a function to each element of an iterable (e.g., a list) and returns a list of results in the same order as the input.
    It blocks until all tasks are completed.
    Suitable when you have a list of inputs and want to parallelize the processing of those inputs, waiting for all results. 
    """
    with mp.Pool(processes=4) as pool:
        result = pool.map(square, range(10))
        print(result)

def map_async():
    """
    similar to map but non-blocking, but returns a MapResult object that can be used to get the result or wait for completion.
    Suitable when you want to map a function over an iterable asynchronously and potentially perform some action when all tasks are finished.
    """
    with mp.Pool(processes=4) as pool:
        result = pool.map_async(square, range(10), callback=lambda x: print(x))
        print(result.get())

def starmap():
    """
    This method is similar to map, but it accepts an iterable of tuples where each tuple contains the arguments for each function call.
    Suitable for cases where you have multiple sets of arguments and want to apply a function to each set concurrently.
    """
    with mp.Pool(processes=4) as pool:
        result = pool.starmap(square, [(0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,)])
        print(result)

def starmap_async():
    """
    Like starmap, but it returns a MapResult object immediately and supports an optional callback.
    Useful for asynchronous concurrent execution of a function with varying sets of arguments.
    """
    with mp.Pool(processes=4) as pool:
        result = pool.starmap_async(square, [(0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,)], callback=lambda x: print(x))
        print(result.get())


if __name__ == '__main__':
    apply()
    apply_async()
    map()
    map_async()
    starmap()
    starmap_async()
