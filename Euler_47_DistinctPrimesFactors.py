# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

from primes import find_primes_less_than


def count_prime_factors(x):
    prime_factor_count = 0
    for prime in primes[:int(x ** 0.5)]:  # only need to check up to the sqrt, this is an approximation
        if x % prime == 0:
            prime_factor_count += 1
    return prime_factor_count


limit = 1000000  # arbitrary large number
primes = find_primes_less_than(int(limit ** 0.5))


for i in [non_prime for non_prime in range(647, limit) if non_prime not in primes]:  # skip to past the givens

    for j in range(4):
        if count_prime_factors(i + j) != 4:
            break
    else:
        print(i)  # 134043
        break
