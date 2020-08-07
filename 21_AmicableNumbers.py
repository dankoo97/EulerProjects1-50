# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b,
# then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

from functools import reduce
from primes import find_primes_less_than


def proper_factors(n):
    # since our numbers are relatively small we just check each number less than sqrt(n) for factors
    factors = list(
        reduce(list.__add__, ([factor, n // factor] for factor in range(1, int(n ** 0.5) + 1) if n % factor == 0))
    )

    factors.sort()

    if int(n ** 0.5) == n ** 0.5:      # if a number has a sqrt it is added to the list twice, 
        factors.remove(int(n ** 0.5))  # so we remove one instance of it

    factors.remove(n)

    return factors


def amicable_pair(val_1):
    val_2 = sum(proper_factors(val_1))
    if val_1 == sum(proper_factors(val_2)) and val_1 != val_2:
        return val_2
    else:
        return False


possible_pairs = list(range(4, 10000))

pairs = []

primes = find_primes_less_than(possible_pairs[-1])

for i in possible_pairs:
    if i in primes:
        possible_pairs.remove(i)  # primes can never be part of an amicable pair, the only proper divisor is 1

while possible_pairs:
    if amicable_pair(possible_pairs[0]):  # we remove checked numbers and numbers that we know have a pair

        pairs += [possible_pairs[0]]
        pairs += [amicable_pair(possible_pairs[0])]

        possible_pairs.remove(amicable_pair(possible_pairs[0]))

    possible_pairs.remove(possible_pairs[0])

print(sum(pairs))  # 31626
