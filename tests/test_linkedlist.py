import unittest
from AKDSFramework.structure.linkedlist import SinglyLinkedList


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.linkedlist = SinglyLinkedList()

    def test_add(self):
        self.linkedlist.add(2)
        self.assertEqual(len(self.linkedlist), 1)
        self.assertEqual(self.linkedlist.get_head().value, 2)

    def test_isEmpty(self):
        self.assertEqual(self.linkedlist.isEmpty(), True)
        self.linkedlist.add(123)
        self.assertEqual(self.linkedlist.isEmpty(), False)

    def test_get_size(self):
        self.assertEqual(len(self.linkedlist), 0)
        self.linkedlist.add(3)
        self.assertEqual(len(self.linkedlist), 1)

    def test_get_head(self):
        self.assertEqual(self.linkedlist.get_head().value, None)
        self.linkedlist.add(4)
        self.assertEqual(self.linkedlist.get_head().value, 4)

    def test_str(self):
        self.linkedlist = SinglyLinkedList()
        self.linkedlist.add(20)
        self.linkedlist.add(120)
        self.linkedlist.add(7102)
        self.linkedlist.add(773)
        self.linkedlist.add('Hello')
        self.assertEqual(str(self.linkedlist), "20 --> 120 --> 7102 --> 773 --> Hello --> None")

    def test_remove(self):
        self.linkedlist = SinglyLinkedList()
        self.linkedlist.add(20)
        self.linkedlist.add(120)
        self.linkedlist.add(7102)
        self.linkedlist.add(773)

        self.assertEqual(str(self.linkedlist), '20 --> 120 --> 7102 --> 773 --> None')
        self.linkedlist.removeAt(0)
        self.assertEqual(str(self.linkedlist), '120 --> 7102 --> 773 --> None')

        self.linkedlist.removeAt(self.linkedlist.count() - 1)
        self.assertEqual(str(self.linkedlist), "120 --> 7102 --> None")

    def test_length(self):
        self.linkedlist = SinglyLinkedList()
        self.linkedlist.add(20)
        self.linkedlist.add(120)
        self.linkedlist.add(7102)
        self.linkedlist.add(773)

        self.assertEqual(len(self.linkedlist), 4)
        self.assertEqual(self.linkedlist.count(), 4)

    def test_getitem(self):
        self.linkedlist = SinglyLinkedList()
        self.linkedlist.add(20)
        self.linkedlist.add(120)
        self.linkedlist.add(7102)
        self.linkedlist.add(773)

        self.assertEqual(self.linkedlist[0], 20)
        self.assertEqual(self.linkedlist[1], 120)
        self.assertEqual(self.linkedlist[2], 7102)
        self.assertEqual(self.linkedlist[3], 773)
