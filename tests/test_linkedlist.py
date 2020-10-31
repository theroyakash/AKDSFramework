import unittest
from AKDSFramework.linkedlist import SinglyLinkedList


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.linkedlist = SinglyLinkedList()

    def test_add(self):
        self.linkedlist.add(2)
        self.assertEqual(len(self.linkedlist), 1)
        self.assertEqual(self.linkedlist.get_head(), 2)

    def test_isEmpty(self):
        self.assertEqual(self.linkedlist.isEmpty(), True)
        self.linkedlist.add(123)
        self.assertEqual(self.linkedlist.isEmpty(), False)

    def test_get_size(self):
        self.assertEqual(len(self.linkedlist), 0)
        self.linkedlist.add(3)
        self.assertEqual(len(self.linkedlist), 1)

    def test_get_head(self):
        self.assertEqual(self.linkedlist.get_head(), None)
        self.linkedlist.add(4)
        self.assertEqual(self.linkedlist.get_head(), 4)

    def test_str(self):
        self.linkedlist = SinglyLinkedList()
        self.linkedlist.add(20)
        self.linkedlist.add(120)
        self.linkedlist.add(7102)
        self.linkedlist.add(773)
        self.linkedlist.add('Hello')
        self.assertEqual(str(self.linkedlist), "['Hello', 773, 7102, 120, 20]")

    def test_remove(self):
        self.linkedlist = SinglyLinkedList()
        self.linkedlist.add(20)
        self.linkedlist.add(120)
        self.linkedlist.add(7102)
        self.linkedlist.add(773)

        self.assertEqual(str(self.linkedlist), '[773, 7102, 120, 20]')
        removed = self.linkedlist.remove()
        self.assertEqual(removed.value, 773)
        self.assertEqual(str(self.linkedlist), '[7102, 120, 20]')

        removed = self.linkedlist.remove()
        self.assertEqual(removed.value, 7102)
        self.assertEqual(str(self.linkedlist), '[120, 20]')

        removed = self.linkedlist.remove()
        self.assertEqual(removed.value, 120)
        self.assertEqual(str(self.linkedlist), '[20]')