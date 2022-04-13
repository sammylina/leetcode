#!/usr/bin/env python3

import unittest

two_sum = __import__('two_sum').two_sum
palindrome = __import__('palindrome').palindrome

class TestDay93(unittest.TestCase):
    
    def test_palindrome(self):
        res = palindrome(121)
        self.assertTrue(res)
        res = palindrome(1235)
        self.assertFalse(res)
        res = palindrome(4)
        self.assertTrue(res)
        res = palindrome(-67876)
        self.assertFalse(res)

    def test_two_sum(self):
        res = two_sum([4, 2, 5, 3, 1], 6)
        self.assertListEqual(res, [0, 1])

        res = two_sum([4, 5, 3], 6)
        self.assertListEqual(res, [])

        res = two_sum([-2, 7, 5, 8], 6)
        self.assertListEqual(res, [0, 3])

