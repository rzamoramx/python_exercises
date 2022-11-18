

class Temperatures:
    def __init__(self, t):
        self._temp = t

    @property
    def temperature(self):
        return self._temp

    @temperature.setter
    def temperature(self, t):
        self._temp = t


if __name__ == '__main__':
    c = Temperatures(500)
    print(c.temperature)

    c.temperature = 1
    print(c.temperature)
