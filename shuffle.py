#!/usr/bin/env python

from itertools import chain
from random import shuffle


def multiply(xs, n): return list(chain.from_iterable([x] * n for x in xs))


def main():
    xs = multiply(['C', 'Haskell', 'Python'], 3)
    shuffle(xs)
    [print(i, x) for (i, x) in enumerate(xs, 1)]


if __name__ == '__main__':
    main()
