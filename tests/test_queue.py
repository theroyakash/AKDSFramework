import unittest
from AKDSFramework.structure.queue import ArrayQueue

class Test(unittest.TestCase):
    def setUp(self):
        self.q = ArrayQueue(4)

    def test_queue_build(self):
        self.assertEqual('[None, None, None, None]', str(self.q))
    
    def test_queue_enqueue(self):
        self.q.enqueue(12)
        self.assertEqual('[12, None, None, None]', str(self.q))
    
    def test_dequeue(self):
        self.q.enqueue(12)
        dqueue = self.q.dequeue()

        self.assertEqual(12, dqueue)

if __name__ == '__main__':
    print('Queue Tests Running')
    unittest.main()
    print('Queue Tests Completed')