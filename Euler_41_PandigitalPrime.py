# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

from pandigital import is_n_pandigital
from primes import find_primes_less_than

# no pandigital prime exists above 7654321 because any pandigital number's sum of digits would be a multiple of 3,
# meaning they are a multiple of 3
primes = find_primes_less_than(7654321)

# since we are looking for the largest, we should go in reverse order,
# and stop at the first truthy value
for p in primes[::-1]:
    if is_n_pandigital(p, len(str(p))):
        print(p)  # 7652413
        break
