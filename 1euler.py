#!/usr/bin/env python

# Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# https://en.wikipedia.org/wiki/Euler_summation
# sum = n(n+1)/2

# https://public.oed.com/how-to-use-the-oed/abbreviations/
# Analyt.	analytic


def max_div_n(n, below):
    return (below - 1) // n


def euler_sum(n):
    return n*(n+1)/2


def euler_sum_max_div(n, below):
    return n*euler_sum(max_div_n(n, below))


def sum_mul_3_5(below):
    return sum((x for x in range(1, below) if x % 3 == 0 or x % 5 == 0))


def main():
    ans = euler_sum_max_div(3, 1000)
    + euler_sum_max_div(5, 1000)
    - euler_sum_max_div(15, 1000)
    print(ans)


if __name__ == '__main__':
    main()
