import unittest
import pyCFB
import numpy as np

class TestCFB(unittest.TestCase):

        def test_case1(self):
            # example from Bovens, L., Chatkupt, C. and Smead, L. (2012)
            # http://fitelson.org/coffey_measure.nb
            p = [0, 0, 1 / 31, 0, 0, 1 / 25, 0, 1 / 4, 0, 1 / 4, 0]
            w = [3 / 355, 1 / 1420, 62 / 71, 21 / 1420, 1 / 1420, 5 / 142, 1 / 710, 1 / 355, 4 / 71, 1 / 355, 1 / 284]
            H_max_ans = 3786 / 126025
            pbar = sum([wi*pi for (pi, wi) in zip(p,w)])
            h = sum([wi*(pi-pbar)**2 for (pi, wi) in zip(p,w)])
            H_ans = np.sqrt(h/H_max_ans)
            H = pyCFB.coffrey(p, w=w)
            self.assertAlmostEqual(H, H_ans, places=4)

if __name__ == '__main__':
    unittest.main()

