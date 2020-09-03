# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
# However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
#
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79.
# The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
# n^2 + an + b, where |a| < 1000 and |b| < 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| == 1 and |-4| == 4
# Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

from primes import find_primes_less_than
primes = find_primes_less_than(100000)


def count_quadratic_primes(a, b):
    if b not in primes:
        return 0  # b must be prime, otherwise at x == 0 f(x) is not prime in f(x) = x^2 + ax + b
    n = 0

    # counts the number of primes in a row
    while n ** 2 + n * a + b in primes:
        n += 1

    return n


longest = 0
A, B = 0, 0


for b in primes:
    if b > 1000:
        break
    # a must be odd otherwise n = 1, n^2 + an + b would be even, and therefore not prime
    # a = 0, b = 2, creates a sequence of two primes, however this is not worthwhile to compare
    for a in range(-999, 1000, 2):  
        length = count_quadratic_primes(a, b)
        if length > longest:
            longest = length
            A, B = a, b


print(A)      # -61
print(B)      # 971
print(A * B)  # -59231
