#!/usr/bin/env python

import math

# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


# Testing algorith in python before haskell

# stolen from http://code.activestate.com/recipes/117119/
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def gen_primes():
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def largest_prime_factor(n, prime=2):
    primes = gen_primes()
    for pr in primes:
        if (pr < prime):
            continue
        if (n == 1):
            return prime
        if (prime > n):
            break
        if (n % pr == 0):
            new_n = n // pr
            return largest_prime_factor(new_n, pr)


def main():
    print(largest_prime_factor(600851475143))


if __name__ == '__main__':
    main()
