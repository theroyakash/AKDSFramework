import unittest
from AKDSFramework.applications.sorting import bubblesort, insertionsort, heapsort, quicksort, merge_sort

class Test(unittest.TestCase):
    def test_bubble_sort(self):
        a = [data for data in range(0, 10)]
        a = bubblesort(a, False, False)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], a)

    def test_insertion_sort(self):
        a = [data for data in range(0, 10)]
        a = insertionsort(a)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], a)

    def test_heap_sort(self):
        a = [data for data in range(0, 10)]
        a = insertionsort(a)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], a)
    
    def test_quicksort_notinplace(self):
        a = [data for data in range(0, 10)]
        a = quicksort(a, False)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], a)

    def test_quicksortinplace(self):
        a = [data for data in range(1, 10)]
        self.assertRaises(NotImplementedError, quicksort, a, True)
    
    def test_merge_sort(self):
        a = [data for data in range(0, 10)]
        a = merge_sort(a)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], a)

if __name__ == '__main__':
    print('Sort tests running')
    unittest.main()