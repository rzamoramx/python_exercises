
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


def test(bird1: Bird):
    """
    Subtypes must be substitutable for their base types without altering the correctness of the program.
    In other words, if you have a base class and a derived class, instances of the derived class should be able to
    replace instances of the base class without causing errors or unexpected behavior. Violating this principle can
    lead to incorrect behavior and make your code difficult to reason about.
    """
    print(bird1.eat())


if __name__ == '__main__':
    penguin = Penguin('Penguin')
    print(penguin.eat())
    print(penguin.make_sound())

    eagle = Eagle('Eagle')
    print(eagle.eat())
    print(eagle.make_sound())
    print(eagle.fly())
    test(eagle)

