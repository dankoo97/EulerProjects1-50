# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

from primes import find_primes_less_than

limit = 1000000
primes = find_primes_less_than(limit)
circular_primes = set(prime for prime in primes[:4])  # putting in single digit primes, use set to eliminate duplicates


def is_circular_prime(p):
    circ = {p, }
    if p in circular_primes:
        return {}
    if any(digit in '024568' for digit in str(p)):  # numbers that end in an even or 5 cannot be prime, except 2 and 5
        return {}
    for permutation in range(1, len(str(p))):
        if int(str(p)[permutation:] + str(p)[:permutation]) not in primes:  # cycles through the given number
            return {}
        circ.add(int(str(p)[permutation:] + str(p)[:permutation]))
    return circ  # returns a set of the circular prime and all its permutations


for prime in primes[4:]:
    c = is_circular_prime(prime)
    if c:
        circular_primes = circular_primes | c

print(len(circular_primes))  # 55
