
# Define a decorator function
def my_decorator(cls):
    class DecoratedClass(cls):
        def __init__(self, *args, **kwargs):
            print("Initializing the object...")
            super().__init__(*args, **kwargs)
            self.extra_attribute = "Hello from the decorator!"
            print("Initialization complete!")

    return DecoratedClass

# Apply the decorator to a class
@my_decorator
class MyClass:
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        print(f"Hello, {self.value}")

# Create an instance of the decorated class
obj = MyClass("World")

# Access the extra attribute added by the decorator
print(obj.extra_attribute)  # Output: Hello from the decorator!

# Call a method of the decorated class
obj.say_hello()  # Output: Hello, World

