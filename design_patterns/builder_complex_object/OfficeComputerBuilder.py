
from design_patterns.builder_complex_object.ComputerBuilder import ComputerBuilder
from design_patterns.builder_complex_object.Computer import Computer


class OfficeComputerBuilder(ComputerBuilder):
    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_gpu(self, gpu):
        print("Office computers don't have GPUs")
        return None

    def set_ram(self, ram):
        if ram > 8:
            raise Exception("Office computers can't have more than 8GB of RAM")
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def build(self):
        return Computer(self.cpu, self.gpu, self.ram, self.storage)
