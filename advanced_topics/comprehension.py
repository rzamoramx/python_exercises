
def multiple():
    print('multiple')
    values = [(x, y) for x in range(5) for y in range(3)]
    print(f'result: {values}')

    # equivalent
    values = []
    for x in range(5):
        for y in range(3):
            values.append((x, y))
    print(f'equivalent: {values}')


def nested():
    print('nested')
    values = [[y*3 for y in range(x)] for x in range(10)]
    print(f'result: {values}')

    # equivalent
    values = []
    for x in range(10):
        inner = []
        for y in range(x):
            inner.append(y*3)
        values.append(inner)
    print(f'equivalent: {values}')


def if_comprehension():
    print('if comprehension')
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd = [num for num in numbers if num % 2 != 0]
    print(f'odd: {odd}')

    # equivalent
    values = []
    for num in numbers:
        if num % 2 != 0:
            values.append(num)
    print(f'equivalent: {values}')


if __name__ == '__main__':
    multiple()
    print('-' * 20)
    nested()
    print('-' * 20)
    if_comprehension()
