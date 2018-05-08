#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""Project Euler - Problem 14.

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import operator

chains = {}

# under one million
for i in range(1, 1000000):
    # if i % 10000 == 0:
    #     print("{}%".format(i / 10000))
    chains[i] = 0
    n = i
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        chains[i] += 1

# print key with biggest value
print(max(chains.iteritems(), key=operator.itemgetter(1))[0])