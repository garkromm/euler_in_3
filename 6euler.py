#!/usr/bin/env python

# Sum square difference
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def diff_sum_squares(n):
    return (sum([x for x in range(1, n+1)])**2 -
            sum([x**2 for x in range(1, n+1)]))


def main():
    print(diff_sum_squares(100))


if __name__ == '__main__':
    main()
