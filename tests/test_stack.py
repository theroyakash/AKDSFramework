import unittest
from AKDSFramework.structure import Stack

class Test(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
    
    def test_push(self):
        for i in range(2, 10):
            self.stack.push(i**2)

        self.assertEqual("4 --> 9 --> 16 --> 25 --> 36 --> 49 --> 64 --> 81 --> None", str(self.stack))
