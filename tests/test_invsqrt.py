import unittest

from AKDSFramework.applications.invsqrt import inv_sqrt

class Test(unittest.TestCase):
    
    def test_case_1(self):
        self.assertAlmostEqual(inv_sqrt(4), 0.499, 3)
        self.assertAlmostEqual(inv_sqrt(16), 0.249, 2)
        self.assertAlmostEqual(inv_sqrt(100), 0.099, 2)
        

if __name__ == '__main__':
    unittest.main()