
import unittest
from data_structures.CustomLinkedList import CustomLinkedList


class CustomLinkedList_test(unittest.TestCase):
    def test_linked_list(self):
        linkedList = CustomLinkedList([1, 2, 3, 4, 5])

        self.assertEqual(linkedList.head.data, 1)

    def test_reverse_linked_list(self):
        linkedList = CustomLinkedList([1, 2, 3, 4, 5])
        reversed_list = linkedList.reverselist(linkedList.head)

        self.assertEqual(reversed_list.data, 5)
        self.assertEqual(reversed_list.next.data, 4)
        self.assertEqual(reversed_list.next.next.data, 3)
        self.assertEqual(reversed_list.next.next.next.data, 2)
        self.assertEqual(reversed_list.next.next.next.next.data, 1)

    def test_print_as_list(self):
        linkedList = CustomLinkedList([1, 2, 3, 4, 5])
        linked_list_as_list = linkedList.print_as_list(linkedList.head)

        self.assertEqual(linked_list_as_list, [1, 2, 3, 4, 5])
