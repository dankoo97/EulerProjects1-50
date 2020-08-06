from primes import find_primes_less_than


def smallest_multiple(x):  # x is the largest number in a series of 1 to x that are factors of the multiple
    i = 1
    factors = []

    while x ** (1 / i) > 2:  # Checks for powers of primes less than the multiple, we use roots to check for powers of primes less than our max multiple
        factors += find_primes_less_than(int(x ** (1 / i)))
        i += 1

    multiple = 1
    for i in factors:
        multiple *= i

    return multiple


print(smallest_multiple(20))  # 232792560
