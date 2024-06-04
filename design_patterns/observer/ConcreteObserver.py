from design_patterns.observer.Observer import Observer


class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} received message: {message}')
