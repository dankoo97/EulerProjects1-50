# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

from primes import find_primes_less_than


def largest_factor(x):
    possible = find_primes_less_than(int(x ** 0.5))  # to save time we only need prime numbers less than the sqrt
    i = 0
    while not (x in possible):
        if x % possible[i] == 0:
            x = int(x / possible[i])
        else:
            i += 1
    return x


print(largest_factor(600851475143))  # 6857
