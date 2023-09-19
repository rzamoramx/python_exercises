
"""
a yield create generator, basically is a function that produces a sequence of
results, maintaining its local state and is capable to resume again exactly
where it left off
"""


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


def pow_two(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
    return n


def generator_in_line():
    pairs = (x for x in range(10) if x % 2 == 0)
    print(type(pairs))
    for pair in pairs:
        print(pair)


if __name__ == '__main__':
    # Using for loop
    for item in my_gen():
        print(item)

    for x in pow_two(4):
        print(f'x: {x}')

    generator_in_line()
