import itertools

# itertools.chain()
# combine two iterables into one
iterable1 = [1, 2, 3]
iterable2 = [4, 5, 6]
chained_iterable = itertools.chain(iterable1, iterable2)
print(list(chained_iterable))  # Output: [1, 2, 3, 4, 5, 6]

# itertools.cycle()
# create an infinite iterator that cycles through a sequence
cycled_iterable = itertools.cycle([1, 2, 3])
for _ in range(6):
    print(next(cycled_iterable))  # Output: 1, 2, 3, 1, 2, 3

# itertools.islice()
# slice an iterable
original_iterable = range(10)
sliced_iterable = itertools.islice(original_iterable, 2, 7)
print(list(sliced_iterable))  # Output: [2, 3, 4, 5, 6]

# itertools.product()
# create the cartesian product of two iterables
product_iterable = itertools.product([1, 2], ['a', 'b'])
print(list(product_iterable))  # Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# itertools.permutations()
# create all permutations of an iterable
# the first parameter of permutations is the iterable, the second parameter is the length of the permutation
permutations_iterable = itertools.permutations([1, 2, 3], 2)
print(list(permutations_iterable))  # Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# itertools.combinations()
# create all combinations of an iterable
# the first parameter of combinations is the iterable, the second parameter is the length of the combination
combinations_iterable = itertools.combinations([1, 2, 3, 4], 2)
print(list(combinations_iterable))  # Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# itertools.groupby()
# group an iterable by a key
# the first parameter is the iterable, the second parameter is the key in this case is a lambda function that returns the first element of the tuple
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
grouped_data = itertools.groupby(data, key=lambda x: x[0])
for key, group in grouped_data:
    print(key, list(group))  # Output: a [('a', 1), ('a', 2)] / b [('b', 3), ('b', 4)]

# itertools.count()
# create an infinite iterator that counts from a number to another number
counter = itertools.count(start=5, step=2)
print(next(counter))  # Output: 5
print(next(counter))  # Output: 7
print(next(counter))  # Output: 9

# itertools.compress()
# filter an iterable based on another iterable of booleans
data = [1, 2, 3, 4, 5]
mask = [True, False, True, False, True]
filtered_data = itertools.compress(data, mask)
print(list(filtered_data))  # Output: [1, 3, 5]

# itertools.filterfalse()
# filter an iterable based on a function that returns False
# the first parameter is the function, the second parameter is the iterable
filtered_false = itertools.filterfalse(lambda x: x % 2 == 0, range(10))
print(list(filtered_false))  # Output: [1, 3, 5, 7, 9]
