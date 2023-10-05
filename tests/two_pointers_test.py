import unittest
from two_pointers import *


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])
        self.assertEqual(two_sum([2, 5, 5, 11], 10), [1, 2])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 2]), 2)
        self.assertEqual(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 1)
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5, 6, 7, 10, 9, 8]), 10)

    def test_sorted_squares(self):
        self.assertEqual(sorted_squares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertEqual(sorted_squares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])
        self.assertEqual(sorted_squares([-1]), [1])
        self.assertEqual(sorted_squares([-1, 0]), [0, 1])

    def test_three_sum(self):
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(three_sum([]), [])
        self.assertEqual(three_sum([0]), [])
        self.assertEqual(three_sum([0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(three_sum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])
        self.assertEqual(three_sum([-2, 0, 1, 1, 2]), [[-2, 0, 2], [-2, 1, 1]])
        self.assertEqual(three_sum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])

    def test_three_sum_closest(self):
        self.assertEqual(three_sum_closest([-1, 2, 1, -4], 1), 2)  # =-4,-1,1,2
        self.assertEqual(three_sum_closest([0, 0, 0], 1), 0)
        self.assertEqual(three_sum_closest([0, 0, 0], 0), 0)
        self.assertEqual(three_sum_closest([0, 0, 0], -1), 0)
        self.assertEqual(three_sum_closest([0, 0, 0], 2), 0)
        self.assertEqual(three_sum_closest([1, 1, 1, 0], -100), 2)
        self.assertEqual(three_sum_closest([1, 1, 1, 0], 100), 3)
        self.assertEqual(three_sum_closest([1, 1, 1, 0], 0), 2)
        self.assertEqual(three_sum_closest([1, 1, 1, 0], 10), 3)
        self.assertEqual(three_sum_closest([-3, -1, 1, 2], 1), 0)

    def test_triplet_with_smaller_sum(self):
        self.assertEqual(three_sum_smaller([-1, 0, 2, 3], 3), 2)
        self.assertEqual(three_sum_smaller([-1, 4, 2, 1, 3], 5), 4)
        self.assertEqual(three_sum_smaller([1, 0, 1, 1], 100), 4)
        self.assertEqual(three_sum_smaller([1, 1, -2, 2, 3], 1), 1)
        self.assertEqual(three_sum_smaller([1, 1, -2, 2, 3], 0), 0)
