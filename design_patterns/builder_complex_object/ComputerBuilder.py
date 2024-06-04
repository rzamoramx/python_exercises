
from abc import ABC, abstractmethod


class ComputerBuilder(ABC):
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None

    @abstractmethod
    def set_cpu(self, cpu):
        pass

    @abstractmethod
    def set_gpu(self, gpu):
        pass

    @abstractmethod
    def set_ram(self, ram):
        pass

    @abstractmethod
    def set_storage(self, storage):
        pass

    @abstractmethod
    def build(self):
        pass
