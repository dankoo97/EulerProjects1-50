def is_n_pandigital(x, n):
    return all(x.count(str(digit)) == 1 for digit in range(1, n + 1)) and '0' not in x


def is_pandigital(x):
    return all(x.count(str(digit)) == 1 for digit in range(1, 10)) and '0' not in x
