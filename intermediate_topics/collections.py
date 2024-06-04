
from collections import *


# Define a namedtuple named "Point" with fields "x" and "y"
Point = namedtuple("Point", ["x", "y"])
p = Point(x=1, y=2)
print(p.x, p.y)  # Output: 1 2



queue = deque()
queue.append(1)  # Add to the end
queue.appendleft(2)  # Add to the beginning
queue.pop()  # Remove and return the last element
queue.popleft()  # Remove and return the first element



string = "abracadabra"
counter = Counter(string)
print(counter)  # Output: Counter({'a': 4, 'b': 2, 'r': 2, 'c': 1, 'd': 1})



d = OrderedDict()
d["a"] = 1
d["b"] = 2
d["c"] = 3
print(d)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])



d = defaultdict(int)  # Default values will be integers (0)
d["a"] += 1
d["b"] += 2
print(d["a"])  # Output: 1
print(d["c"])  # Output: 0 (default value)



dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
combined_dict = ChainMap(dict1, dict2)
print(combined_dict["a"])  # Output: 1
print(combined_dict["b"])  # Output: 2 (from dict1)
print(combined_dict["c"])  # Output: 4




class MyDict(UserDict):
    def __missing__(self, key):
        return f"Key '{key}' not found"

my_dict = MyDict({"a": 1, "b": 2})
print(my_dict["a"])  # Output: 1
print(my_dict["c"])  # Output: Key 'c' not found

class ValidatedDict(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Keys must be strings")
        super().__setitem__(key, value)

# Usage
validated_dict = ValidatedDict()
validated_dict["name"] = "John"
validated_dict[42] = "Invalid"  # Raises ValueError





class MyList(UserList):
    def append_twice(self, value):
        self.append(value)
        self.append(value)

my_list = MyList([1, 2, 3])
my_list.append_twice(4)
print(my_list)  # Output: [1, 2, 3, 4, 4]

class FilteredList(UserList):
    def filter_positive(self):
        return FilteredList([x for x in self.data if x > 0])

# Usage
my_list = FilteredList([1, -2, 3, -4])
positive_numbers = my_list.filter_positive()
print(positive_numbers)  # Output: [1, 3]





class MyString(UserString):
    def reverse(self):
        return self.data[::-1]

my_string = MyString("hello")
reversed_string = my_string.reverse()
print(reversed_string)  # Output: olleh

class FormattedString(UserString):
    def reverse_and_format(self):
        reversed_string = self.data[::-1]
        return f"Reversed: {reversed_string}"

# Usage
my_string = FormattedString("hello")
formatted = my_string.reverse_and_format()
print(formatted)  # Output: Reversed: olleh

