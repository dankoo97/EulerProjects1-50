# Uses Sieve of Eratosthenes to find primes
def find_primes_less_than(x):
    p = [True] * (x >> 1)  # Creates a boolean list of odd numbers
    primes = [2]  # Create the final list of primes, 2 is added since only odd numbers are checked

    i = 0
    while i < (int(x ** 0.5) >> 1):  # Only checking up until sqrt of x
        if p[i]:
            primes.append((i << 1) + 3)
            p = [prime if ((j << 1) + 3) % primes[-1] != 0 else False for j, prime in enumerate(p)]  # removes multiples of the latest prime from list
        i += 1

    for i, prime in enumerate(p):  # Adds all True values from p and converts them into numbers
        if prime:
            primes.append((i << 1) + 3)

    if primes[-1] > x:  # Only used if x is one less than a prime
        return primes[:-1]
    else:
        return primes


def xth_prime(x):
    if x == 1:
        return 2
    if x == 2:
        return 3

    primes = [2, 3]
    i = 5

    while len(primes) < x:
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
        i += 2

    return primes[-1]
