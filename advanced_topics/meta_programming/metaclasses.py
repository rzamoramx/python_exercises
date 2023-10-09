"""
metaclasses are a meta programming powerful tool that allow us to define the behavior of classes
in other words, while classes define the behavior of objects, metaclasses define the behavior of classes
at runtime.

you can think of metaclasses as the blueprints of classes, just like classes are the blueprints of objects.

key points:

- everything in python is an object, including classes
- you can add attributes and methods or modify class behavior at runtime
- often used for validation, enforce coding standards, logging, registering classes, etc.
"""

class MyMeta(type):
    def __init__(cls, name, bases, attrs):
        if "my_attr" not in attrs:
            raise TypeError("bad user class")
        super().__init__(name, bases, attrs)

class MyClass(metaclass=MyMeta):
    other_atter = 1
    def my_method(self):
        return self.my_attr
    
obj = MyClass()
print(obj.my_method())
