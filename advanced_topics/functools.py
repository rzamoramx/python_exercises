from functools import partial, wraps
from functools import lru_cache

# ********** partial **********

# the partial is used to create a new function with some default arguments
# original function
def power(base, exponent):
    return base ** exponent

# it creates a new function with the same name but with the default argument
square = partial(power, exponent=2)
result = square(5) # this calculates 5^2
print(result) # Output: 25

# ********** wraps **********

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("print before call function")
        result = func(*args, **kwargs)
        print("print after call function")
        return result
    return wrapper


@my_decorator
def say_hello():
    print("Hello")

# ********** lru_cache **********

@lru_cache(maxsize=2)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))  # calculates and caches fibonacci(0) to fibonacci(5)
print(fibonacci(3))  # Get saved value for fibonacci(3)

# ********** reduce **********

from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 120 (1 * 2 * 3 * 4 * 5)

# ********** partial method **********

from functools import partialmethod

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def _area(self, pi, radius):
        return pi * radius ** 2
    
    area = partialmethod(_area, 3.14159265359)  # Fija el valor de pi
    
circle = Circle(5)
print(circle.area())  

# ********** cmp to key **********

from functools import cmp_to_key

def compare_length(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    return 0

names = ["Alice", "Bob", "Charlie", "David"]
sorted_names = sorted(names, key=cmp_to_key(compare_length))
print(sorted_names)  # Output: ['Bob', 'Alice', 'David', 'Charlie']

# ********** ordering **********

from functools import total_ordering

@total_ordering
class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __eq__(self, other):
        return (self.numerator / self.denominator) == (other.numerator / other.denominator)
    
    def __lt__(self, other):
        return (self.numerator / self.denominator) < (other.numerator / other.denominator)

r1 = Rational(1, 2)
r2 = Rational(2, 3)
print(r1 < r2)  # Output: True

# ********** singledispatch **********

from functools import singledispatch

@singledispatch
def my_func(arg):
    print('default my_func({!r})'.format(arg))

my_func('string argument')


