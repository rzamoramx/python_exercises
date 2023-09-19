
from design_patterns.builder_complex_object.GamingComputerBuilder import GamingComputerBuilder


class ComputerDirector:
    def build_gaming_computer(self):
        return GamingComputerBuilder()\
            .set_cpu("Intel i7")\
            .set_gpu("Nvidia RTX 2080")\
            .set_ram(32)\
            .set_storage(1000)\
            .build()
    
    def build_office_computer(self):
        return GamingComputerBuilder()\
            .set_cpu("Intel i3")\
            .set_ram(8)\
            .set_storage(500)\
            .build()
