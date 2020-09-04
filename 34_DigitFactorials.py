# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

import math

digit_factorials = [math.factorial(i) for i in range(10)]
factorial_sums = set()

# upperbound of 6 digits because 7 * 9! because 7 * 9! == 2540160 < 9999999 (7 9s)
# can quickly eliminate all 2 digit numbers, all digits would need to be below 5, include 4, and between 25 and 30
# could possibly make more efficient by restricting the range to only possible to reach numbers with however many additions
# ie. 2881 - 5039 are impossible to reach with only 4 digits, as 6! * 4 == 2880 and 7! == 5040
for i in range(125, 1000000):
    if i == sum(digit_factorials[int(digit)] for digit in str(i)):
        factorial_sums.add(i)

print(sum(factorial_sums))  # 40730  {145, 40585}
