#!/usr/bin/env python

import unittest

# Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# https://en.wikipedia.org/wiki/Euler_summation
# sum = n(n+1)/2


def max_div_n(n, below):
    return (below - 1) // n


def euler_sum(n):
    return n*(n+1)/2


def sum_mul_3_5_anal(below):
    max_div_3, max_div_5, max_div_15 = max_div_n(
        3, below), max_div_n(5, below), max_div_n(15, below)
    final_sum = 3*euler_sum(max_div_3) + 5 * \
        euler_sum(max_div_5) - 15*euler_sum(max_div_15)
    return int(final_sum)


def sum_mul_3_5(below):
    return sum((x for x in range(1, below) if x % 3 == 0 or x % 5 == 0))


class Tests(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum_mul_3_5(10), 23, "Should be 23")

    def test_sum_anal(self):
        self.assertEqual(sum_mul_3_5_anal(10), 23, "Should be 23")

    def test_euler_sum(self):
        self.assertAlmostEqual(euler_sum(100), sum(range(1, 101)))


def main():
    print(sum_mul_3_5_anal(1000))


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
