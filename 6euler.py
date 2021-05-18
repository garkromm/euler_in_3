#!/usr/bin/env python

# Sum square difference
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

# https://proofwiki.org/wiki/Sum_of_Sequence_of_Squares
# https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF


def diff_sum_squares(n):
    return (sum([x for x in range(1, n+1)])**2 -
            sum([x**2 for x in range(1, n+1)]))


def diff_sum_squares_analyt(n):
    return int(sum_n(n)**2 - sum_n_2(n))


def sum_n(n):
    return n*(n+1)/2


def sum_n_2(n):
    return n*(n+1)*(2*n+1)/6


def main():
    print(diff_sum_squares(100))
    print(diff_sum_squares_analyt(100))
    print(diff_sum_squares(100) == diff_sum_squares_analyt(100))


if __name__ == '__main__':
    main()
