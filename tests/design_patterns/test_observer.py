
import unittest
from design_patterns.observer.ConcreteSubject import ConcreteSubject
from design_patterns.observer.ConcreteObserver import ConcreteObserver


class TestObserver(unittest.TestCase):
    """
    The Observer Pattern is a behavioral design pattern that defines a one-to-many dependency between objects so that
    when one object changes state, all its dependents (observers) are notified and updated automatically. This pattern
    is used to maintain consistency between related objects without making them tightly coupled

    the implementation code is located in the design_patterns/observer package
    """
    def test_observer(self):
        subject = ConcreteSubject()
        observer1 = ConcreteObserver('Observer 1')
        observer2 = ConcreteObserver('Observer 2')
        subject.attach(observer1)
        subject.attach(observer2)
        subject.state = 'state 1'
        subject.detach(observer2)
        subject.state = 'state 2'
