import unittest
from AKDSFramework.structure.heap import MaxHeap, MinHeap
from AKDSFramework.error import HeapNotBuildError, InvalidOperationError

class TestQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.mnheap = MinHeap([data**3 for data in range(1, 15)])
        self.mxheap = MaxHeap([data**3 for data in range(1, 15)])

    def test_add_maxHeap(self):
        self.mxheap.add(12)
        self.mxheap.add(4)
        self.mxheap.build()

        self.assertEqual('[2744, 1331, 2197, 729, 1000, 1728, 343, 512, 64, 8, 125, 1, 216, 27, 12, 4]',
                         str(self.mxheap))

    def test_add_minHeap(self):
        self.mnheap.add(12)
        self.mnheap.add(4)
        self.mnheap.build()
        self.assertEqual('[1, 4, 12, 8, 125, 216, 27, 64, 729, 1000, 1331, 1728, 2197, 2744, 343, 512]',
                         str(self.mnheap))

    def test_heapnotbuilderror(self):
        self.mxheap.add(12)
        self.mxheap.add(4)

        # HeapNotBuildError raise check
        self.assertRaises(HeapNotBuildError, print, self.mxheap)

        self.mnheap.add(12)
        self.mnheap.add(4)

        # HeapNotBuildError raise check
        self.assertRaises(HeapNotBuildError, print, self.mnheap)

    def test_len(self):
        self.mnheap.add(12)
        self.mnheap.add(4)
        self.mnheap.build()

        self.mxheap.add(12)
        self.mxheap.add(4)
        self.mxheap.build()

        self.assertEqual(16, len(self.mnheap))
        self.assertEqual(16, len(self.mxheap))

    def test_reversed_raises_error(self):
        self.assertRaises(InvalidOperationError, reversed, self.mxheap)
        self.assertRaises(InvalidOperationError, reversed, self.mnheap)

    def test_getitem(self):
        self.mnheap.add(12)
        self.mnheap.add(4)

        self.mnheap.build()
        self.assertEqual(self.mnheap[1], 4)

        self.mxheap.add(12)
        self.mxheap.add(4)
        self.mxheap.build()

        self.assertEqual(self.mxheap[1], 1331)


if __name__ == '__main__':
    unittest.main()
