# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from primes import find_primes_less_than

primes = find_primes_less_than(1000000)  # picked an arbitrary large number, if needed we can make it larger


def is_truncatable_prime(p):
    if any(digit in '0468' for digit in str(p)[:-1]):  # if these numbers are in at any point it cant be
        return False
    if any(digit in '25' for digit in str(p)[1:-1]):  # 2 and 5 can only come at the beginning of the number
        return False
    for digit in range(1, len(str(p))):  # checks each truncation for primeness
        if int(str(p)[digit:]) not in primes or int(str(p)[:digit]) not in primes:
            return False
    return True


truncatable_primes = set()

for prime in primes[4:]:  # skip single digits
    if is_truncatable_prime(prime):
        truncatable_primes.add(prime)


print(sum(truncatable_primes))  # 748317
