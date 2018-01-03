import unittest
from unittest import TestCase
from Matrix import M

class TestLast(unittest.TestCase):
    def test_str(self):
        m = M(2, 1)
        m.m = [[1, 2], [3, 4]]
        result = M.__str__(m)
        self.assertEqual(result, "1 2 \n3 4 \n")

    def test_maindiag(self):
        m = M(2, 1)
        m.m = [[1, 2], [3, 4]]
        self.assertEqual(m.maindiag(), 5)

    def test_trans(self):
        m = M(2, 1)
        m.m = [[1, 2], [3, 4]]
        m.m=m.trans()
        dopm=[[1,3],[2,4]]
        self.assertEqual(m.m, dopm)
    def test_lt(self):
        m1 = M(2, 1)
        m1.m = [[1, 2], [3, 4]]
        m2 = M(2, 1)
        m2.m = [[2, 3], [4, 5]]
        self.assertTrue(m1<m2)
    def test_gt(self):
        m1 = M(2, 1)
        m1.m = [[1, 2], [3, 4]]
        m2 = M(2, 1)
        m2.m = [[2, 3], [4, 5]]
        self.assertTrue(m2>m1)
    def test_eq(self):
        m1 = M(2, 1)
        m1.m = [[1, 2], [3, 4]]
        m2 = M(2, 1)
        m2.m = [[2, 3], [4, 5]]
        self.assertFalse(m1==m2)
    def test_add(self):
        m1 = M(2, 1)
        m1.m = [[1, 2], [3, 4]]
        m2 = M(2, 1)
        m2.m = [[2, 3], [4, 5]]
        dopm=[[3,5],[7,9]]
        self.assertEqual(m1+m2, dopm)
if __name__ == '__main__':
    unittest.main()