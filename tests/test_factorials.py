import unittest
from AKDSFramework.applications import factorials

class TestQueue(unittest.TestCase):
    def test_factorials_iter(self):
        self.assertEqual(120, factorials(5, True))

    def test_factorials_recur(self):
        self.assertEqual(120, factorials(5, False))

    def test_error_raise(self):
        self.assertRaises(ValueError, factorials, -10)

if __name__ == "__main__":
    unittest.main()