
import unittest
from design_patterns.builder_complex_object.GamingComputerBuilder import GamingComputerBuilder
from design_patterns.builder_complex_object.ComputerDirector import ComputerDirector


class TestBuilderComplexObject(unittest.TestCase):
    """
    The Builder Pattern is a creational design pattern that lets you construct complex objects step by step. The
    pattern allows you to produce different types and representations of an object using the same construction code.

    the implementation code is located in the design_patterns/builder_complex_object package
    """

    def test_gaming_computer_without_builder_helper(self):
        computer = GamingComputerBuilder()\
            .set_cpu("Intel i7")\
            .set_gpu("Nvidia RTX 2080")\
            .set_ram(32)\
            .set_storage(1000)\
            .build()

        self.assertEqual(computer.cpu, "Intel i7")
        self.assertEqual(computer.gpu, "Nvidia RTX 2080")
        self.assertEqual(computer.ram, 32)
        self.assertEqual(computer.storage, 1000)

    def test_gaming_computer_with_builder_helper(self):
        computer = ComputerDirector().build_gaming_computer()

        self.assertEqual(computer.cpu, "Intel i7")
        self.assertEqual(computer.gpu, "Nvidia RTX 2080")
        self.assertEqual(computer.ram, 32)
        self.assertEqual(computer.storage, 1000)

    def test_office_computer_with_builder_helper(self):
        computer = ComputerDirector().build_office_computer()

        self.assertEqual(computer.cpu, "Intel i3")
        self.assertEqual(computer.gpu, None)
        self.assertEqual(computer.ram, 8)
        self.assertEqual(computer.storage, 500)

    def test_fail_office_computer_exceeds_ram_limit(self):
        with self.assertRaises(Exception):
            ComputerDirector().build_office_computer().set_ram(16)

