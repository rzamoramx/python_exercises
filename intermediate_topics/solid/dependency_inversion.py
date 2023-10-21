
from abc import ABC, abstractmethod

"""
The SOLID principles are
- Single Responsibility Principle
- Open/Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle

in this example we will see the Dependency Inversion Principle, see comments below
"""


class BillingRepository(ABC):
    @abstractmethod
    def save(self, order):
        pass


class DatabaseBillingRepository(BillingRepository):
    def save(self, order):
        return f'Saving {order} in the database'


class OtherBillingRepository(BillingRepository):
    def save(self, order):
        return f'Saving {order} in other place'


class BillingService:
    """
    this principle encourages us to make that high level classes don't depend on low level classes, instead they should
    depend on abstractions, so we can inject the dependencies in the class that needs them, inverting the control of
    the dependencies, we can use many manners to inject the dependencies, in this case we are using the constructor
    we can use setter methods or even properties
    """
    def __init__(self, billing_repository: BillingRepository):
        self.billing_repository = billing_repository

    def save(self, order):
        return self.billing_repository.save(order)


if __name__ == '__main__':
    billing_service = BillingService(DatabaseBillingRepository())
    print(billing_service.save('order'))

    billing_service = BillingService(OtherBillingRepository())
    print(billing_service.save('order'))
