import unittest
from AKDSFramework.applications.sorting import bubblesort, insertionsort

class Test(unittest.TestCase):
    def test_bubble_sort(self):
        a = [data for data in range(0, 10)]
        a = bubblesort(a, False, False)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], a)

    def test_insertion_sort(self):
        a = [data for data in range(0, 10)]
        a = insertionsort(a)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], a)


if __name__ == '__main__':
    print('Sort tests running')
    unittest.main()