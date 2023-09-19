from design_patterns.observer.Subject import Subject


class ConcreteSubject(Subject):
    def __init__(self):
        self._observers = set()
        self._state = None

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.discard(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        if state != self._state:
            self._state = state
            self.notify()
