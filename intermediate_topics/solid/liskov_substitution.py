
"""
The SOLID principles are
- Single Responsibility Principle
- Open/Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle

in this example we will see the Liskov Substitution Principle, see comments below
"""


class Bird:
    def __init__(self, name):
        self.name = name

    # This method definition here, breaks the principle, because the subclass Penguin can't fly, and we can be tempted
    # to throw an exception in the subclass Penguin for this method, but this is not the correct way to implement the
    # principle
    # def fly(self):
    #    return f'{self.name} can fly'

    def eat(self):
        return f'{self.name} can eat'


class FlyingBird(Bird):
    # this is the correct way to implement the principle
    def fly(self):
        return f'{self.name} can fly'


class Penguin(Bird):
    # this type of bird can't fly
    def make_sound(self):
        return f'{self.name} can make sound of a penguin'


class Eagle(FlyingBird):
    # this type of bird can fly
    def make_sound(self):
        return f'{self.name} can make sound of an eagle'


def test(bird1: Eagle):
    # bird1 is hinting that it is an Eagle, but it can be a Bird or a FlyingBird, because they are subclasses of Eagle
    # so with Liskov Substitution Principle we can use the subclasses of a class without changing the behavior
    # this is specially noticeable in strongly typed languages like Java or C#
    print(bird1.eat())


if __name__ == '__main__':
    bird = Bird('Bird')
    test(bird)

    penguin = Penguin('Penguin')
    print(penguin.eat())
    print(penguin.make_sound())
    # print(penguin.fly())

    eagle = Eagle('Eagle')
    print(eagle.eat())
    print(eagle.make_sound())
    print(eagle.fly())

