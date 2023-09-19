
class Computer:
    def __init__(self, cpu, gpu, ram, storage):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.storage = storage

    def __str__(self):
        return f"Computer [CPU: {self.cpu}, GPU: {self.gpu}, RAM: {self.ram}GB, Storage: {self.storage}GB]"
