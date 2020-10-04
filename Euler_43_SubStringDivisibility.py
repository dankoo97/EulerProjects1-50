# The number, 1406357289, is a 0 to 9 pandigital number
# because it is made up of each of the digits 0 to 9 in some order,
# but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
# In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.
from primes import find_primes_less_than
from itertools import permutations

primes = find_primes_less_than(18)


def is_substring_divisible(x):
    for index, prime in enumerate(primes, 1):
        if int(x[index: index+3]) % prime != 0:
            return False
    return True


permutation = 0
# brute force, check each permutation, some optimizations could reduce number of checks
for p in permutations(range(10)):
    if is_substring_divisible(str(p)[1::3]):
        permutation += int(str(p)[1::3])

print(permutation)  # 16695334890
