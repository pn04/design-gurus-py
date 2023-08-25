import unittest
from warmup import *


class TestWarmup(unittest.TestCase):
    def test_contains_duplicate(self):
        self.assertEqual(contains_duplicate([1, 2, 3, 4, 5]), False)
        self.assertEqual(contains_duplicate([1, 2, 3, 4, 5, 1]), True)
        self.assertEqual(contains_duplicate([1, 2, 3, 4, 5, 2]), True)
        self.assertEqual(contains_duplicate([1, 2, 3, 4, 5, 3]), True)
        self.assertEqual(contains_duplicate([1, 2, 3, 4, 5, 4]), True)
        self.assertEqual(contains_duplicate([1, 2, 3, 4, 5, 5]), True)
        self.assertEqual(contains_duplicate([1, 2, 3, 4, 5, 6]), False)

    def test_is_pangram(self):
        self.assertEqual(
            is_pangram("The quick brown fox jumps over the little lazy dog"), True
        )
        self.assertEqual(
            is_pangram("The quick brown fox jumps over the lazy cat"), False
        )
        self.assertEqual(
            is_pangram("The quick brown fox jumps over the lazy dog."), True
        )
        self.assertEqual(
            is_pangram("The quick brown fox jumps over the lazy dog!"), True
        )

    def test_square_root(self):
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(2), 1)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(5), 2)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(10), 3)
        self.assertEqual(square_root(11), 3)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(19), 4)

    def test_reverse_vowels(self):
        self.assertEqual(reverse_vowels("hello"), "holle")
        self.assertEqual(reverse_vowels("leetcode"), "leotcede")

    def test_is_valid_palindrome(self):
        self.assertEqual(is_valid_palindrome("Was it a car or a cat I saw?"), True)
        self.assertEqual(is_valid_palindrome("0P"), False)

    def test_is_anagram(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True)
        self.assertEqual(is_anagram("rat", "car"), False)
        self.assertEqual(is_anagram("a", "ab"), False)
        self.assertEqual(is_anagram("ab", "a"), False)

    def test_shortest_word_distance(self):
        self.assertEqual(
            shortest_word_distance(
                ["practice", "makes", "perfect", "coding", "makes"],
                "coding",
                "practice",
            ),
            3,
        )
        self.assertEqual(
            shortest_word_distance(
                ["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"
            ),
            1,
        )

    def test_num_of_good_pairs(self):
        self.assertEqual(num_of_good_pairs([1, 2, 3, 1, 1, 3]), 4)
        self.assertEqual(num_of_good_pairs([1, 1, 1, 1]), 6)
        self.assertEqual(num_of_good_pairs([1, 2, 3]), 0)
