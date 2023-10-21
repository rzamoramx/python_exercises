
from abc import ABC, abstractmethod

"""
The SOLID principles are
- Single Responsibility Principle
- Open/Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle

in this example we will see the Interface Segregation Principle, see comments below
"""


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    # the problem with this method is that not all printers can scan, so we are forcing the subclasses to implement
    # this method, and this breaks the principle
    #@abstractmethod
    #def scan(self, document):
    #    pass


# the principle encourages us to write multiple interfaces instead of one, segregating the methods in different
# interfaces
class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class SpecificPrinter(Printer):
    def print(self, document):
        return f'Printing {document}'


class SpecificScanner(Scanner):
    def scan(self, document):
        return f'Scanning {document}'


class MultiFunctionPrinter(Printer, Scanner):
    def print(self, document):
        return f'Printing {document}'

    def scan(self, document):
        return f'Scanning {document}'


if __name__ == '__main__':
    printer = SpecificPrinter()
    print(printer.print('document'))

    scanner = SpecificScanner()
    print(scanner.scan('document'))

    multi_function_printer = MultiFunctionPrinter()
    print(multi_function_printer.print('document'))
    print(multi_function_printer.scan('document'))
