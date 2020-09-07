# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

from primes import find_primes_less_than
import itertools


primes = find_primes_less_than(10000)[168:]  # primes[168] == 1009, the first 4 digit prime
solutions = set()

for prime in primes:
    # create a list of all permutations of a prime
    permutations = [pr for pr in primes if tuple(str(pr)) in itertools.permutations(str(prime))]

    if len(permutations) >= 3:

        for combo in itertools.combinations(permutations, 3):
            # we check each combo for the arithmetic conditions
            if combo[1] - combo[0] == combo[2] - combo[1]:
                solutions.add(combo)
                break

for solution in solutions:
    print(*solution, sep='')  # 296962999629, we ignore the given 148748178147
