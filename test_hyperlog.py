import unittest
from hyperlog import HyperLog

class TestHyperlog(unittest.TestCase):
    def setUp(self):
        self.hyperlog = HyperLog(4)

    def test_count_leading_zero(self):
        num = int("000011", 2)
        k = 6
        expect = 4
        actual = self.hyperlog.count_leading_zero(num, k)
        self.assertEqual(expect, actual)

