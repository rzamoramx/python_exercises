
from abc import ABCMeta, abstractmethod

"""
factory pattern example
"""


class Animal(metaclass=ABCMeta):
    """
    animal interface
    """
    @abstractmethod
    def do_say(self) -> str:
        pass


class Dog(Animal):
    def do_say(self):
        return "Bhow Bhow!!"


class Cat(Animal):
    def do_say(self):
        return "Meow Meow!!"


class AnimalFactory:
    """
    animal factory class
    """
    def create_animal(self, animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")


# usage
if __name__ == "__main__":
    animal_factory = AnimalFactory()

    dog = animal_factory.create_animal("dog")
    print(dog.do_say())

    cat = animal_factory.create_animal("cat")
    print(cat.do_say())
