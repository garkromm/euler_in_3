#!/usr/bin/env python
from math import log2, floor
import random
from decimal import Decimal

# St. Petersburg Lottery
#
# A gambler decides to participate in a special lottery. In this lottery the
# gambler plays a series of one or more games.
# Each game costs m pounds to play and starts with an initial pot of 1 pound.
# The gambler flips an unbiased coin. Every time a head appears, the pot is
# doubled and the gambler continues. When a tail appears, the game ends and
# the gambler collects the current value of the pot. The gambler is certain to
# win at least 1 pound, the starting value of the pot, at the cost of m pounds,
# the initial fee.
# The game ends if the gambler's fortune falls below m pounds. Let pm(s)
# denote the probability that the gambler will never run out of money in
# this lottery given an initial fortune s and the cost per game m.
# For example p2(2) ≈ 0.2522, p2(5) ≈ 0.6873 and p6(10 000) ≈ 0.9952
# (note: pm(s) = 0 for s < m).
# Find p15(109) and give your answer rounded to 7 decimal places behind
# the decimal point in the form 0.abcdefg.


def prob_loss(m, s):
    if (m > s):
        return 0
    prob_loss = []
    count = 1
    while (count < 10):
        prob_loss.append(games_till_loss_calc(m, s))
        count += 1
    return Decimal(sum(prob_loss))/Decimal(len(prob_loss))


def games_till_loss_calc(m, s):
    count = 1
    bankroll = 1
    win = 0
    casinoMaxGames = floor(log2(s))
    while(count <= casinoMaxGames):
        if random.random() > 0.5:
            bankroll *= 2
            # print('H')
        else:
            s += bankroll - m
            bankroll = 1
            # print('T')
        print(f'bankroll {bankroll}, stack {s}, count {count}')

        count += 1

    return win


def main():
    print(prob_loss(15, 1e+9))


if __name__ == '__main__':
    main()
