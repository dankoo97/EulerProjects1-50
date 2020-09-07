# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from primes import find_primes_less_than

limit = 10000

primes = find_primes_less_than(limit)         # we generate arbitrarily large lists, of number to iterate through
squares = [i ** 2 for i in range(1, limit)]

for odd in [i for i in range(9, limit, 2) if i not in primes]:
    for square in squares[:int((odd // 2) ** 0.5)]:  # comparing to negatives is wasteful
        if odd - (2 * square) in primes:
            break
    else:
        print(odd)  # 5777
        break

