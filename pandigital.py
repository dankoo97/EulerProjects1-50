def is_n_pandigital(x, n):
    return all(str(x).count(str(digit)) == 1 for digit in range(1, n + 1)) and '0' not in str(x)


def is_pandigital(x):
    return all(str(x).count(str(digit)) == 1 for digit in range(1, 10)) and '0' not in str(x)


def is_0_to_n_pandigital(x, n=9):
    return all(str(x).count(str(digit)) == 1 for digit in range(0, n + 1))
