# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math

dig = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def xth_permutation(x, digits):  # calculates the number of permutations recursively by appending digits
    if x > math.factorial(len(digits)):  # Number of possible permutations == factorial(number of digits)
        return False

    if len(digits) == 1:
        return digits[0]  # if there is only one digit return it

    digits.sort()  # make sure we have the first lexicographical permutation
    perm = 1

    n = 0
    for i in range(1, len(digits) + 1):
        perm *= i
        if perm >= x:  # checks whether our permutation is with i! number of permutations
            print(str(i) + "!")
            n = (x - 1) // math.factorial(i - 1)  # we use floor division to see how many times the previous number factorial goes into x, this gives us our next digit
            x = x - n * math.factorial(i - 1)  # the number more permutations left to calculate after this digit
            break
    print("Next digit", digits[n])
    print(x)
    n = digits[n]
    digits.remove(n)  # this digit is no longer available so we remove it
    print(digits)  # available digits
    return str(n) + str(xth_permutation(x, digits))  # recursively find the xth permutation with the remaining digits


print(xth_permutation(1000000, dig))  # 2783915460
