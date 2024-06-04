import operator
import time
import itertools

"""
Itertools provides a number of functions that help in writing clean, fast, and memory-efficient code due to lazy 
evaluation, some of this functions are count(), cycle(), repeat(), accumulate(), product(), permutations(), 
mul(), combinations() etc.
"""

def repeat():
    print(list(itertools.repeat("Hi!", 5)))


def infinite_cycle_using_next():
    li = ['One', 'Two', 'Three']

    # defining iterator
    iterator = itertools.cycle(li)

    for _ in range(8):
        # Using next function
        print(next(iterator), end=" ")
    print(' ')


def infinite_cycle():
    # infinite loop, until break at count > 7
    count = 0
    for i in itertools.cycle('AB'):
        if count > 7:
            break
        else:
            print(i, end=" ")
            count += 1
    print(' ')


def infinite_count():
    # count 5 by 5, until break at 35
    for i in itertools.count(5, 5):
        if i == 35:
            break
        else:
            print(i, end=" ")
    print(' ')


def mul():
    # Defining lists
    l1 = [1, 2, 3]
    l2 = [2, 3, 4]

    # Starting time before map function
    t1 = time.time()

    # Calculating result
    a, b, c = map(operator.mul, l1, l2)

    # Ending time after map function
    t2 = time.time()

    # Time taken by map function
    print("Result:", a, b, c)
    print("Time taken by map function: %.6f" %(t2 - t1))

    # Starting time before naive method
    t1 = time.time()

    # Calculating result using for loop
    print("Result:", end=" ")
    for i in range(3):
        print(l1[i] * l2[i], end = " ")

    # Ending time after naive method
    t2 = time.time()
    print("\nTime taken by for loop: %.6f" % (t2 - t1))


if __name__ == '__main__':
    mul()
    print('-'*40)
    infinite_count()
    print('-'*40)
    infinite_cycle()
    print('-'*40)
    infinite_cycle_using_next()
    print('-'*40)
    repeat()
