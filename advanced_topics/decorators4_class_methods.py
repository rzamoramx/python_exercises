from datetime import date


class Person:
    name = ""
    age = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self):
        """
        normal class method, related to a instance and is necessary to instantiate
        the class
        """
        return self.name

    @classmethod
    def from_birth_year(cls, name: str, year: int):
        """
        the main use case is for multiple constructors of a class, it is useful
        for polymorphism, this func is related to class not an instance
        """
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        """
        the main use case is for utilities that doesn't require an instance
        of the class, this func is related to a instance not a class, but is not
        necessary to instantiate to access it
        """
        return age > 18
