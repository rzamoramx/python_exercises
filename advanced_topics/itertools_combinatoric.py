import itertools


def permutations():
    print('permutations of string:')
    print(list(itertools.permutations([2, "hi"], 2)))
    print('permutations of string:')
    print(list(itertools.permutations('ABC')))
    print('permutations of container')
    print(list(itertools.permutations(range(3), 3)))


def product():
    # Cartesian product using repeat
    print('cartesian product using repeat param:')
    print(list(itertools.product([1, 2, 3], repeat=2)))

    # Cartesian product using containers
    print('cartesian product of the containers:')
    print(list(itertools.product([2, 3, 4], '51')))
    print(list(itertools.product('AC', [5, 6])))


if __name__ == '__main__':
    product()
    print('-'*40)
    permutations()
