
from design_patterns.builder_complex_object.ComputerBuilder import ComputerBuilder
from design_patterns.builder_complex_object.Computer import Computer


class GamingComputerBuilder(ComputerBuilder):
    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_gpu(self, gpu):
        self.gpu = gpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def build(self):
        return Computer(self.cpu, self.gpu, self.ram, self.storage)
