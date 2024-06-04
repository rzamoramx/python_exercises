
"""
The SOLID principles are
- Single Responsibility Principle
- Open/Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle

In this class we will see the Single Responsibility Principle, see comments below
"""


class SingleResponsability:
    """
    This principle encourages us to write classes that have only one responsability. for example this class
    only has two responsabilities no more:
    1. To manage the user
    2. To manage the user's data
    """

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def get_user(self):
        return self.name, self.age, self.email

    def set_user(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def get_user_data(self):
        return self.name, self.age

    def set_user_data(self, name, age):
        self.name = name
        self.age = age