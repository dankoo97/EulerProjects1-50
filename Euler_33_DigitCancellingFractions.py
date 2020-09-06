# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
# which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, 
# and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
import functools

lcd = []

# we iterate through all possible combinations
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            # ignoring trivial examples ie. 11/22 or 30/50
            if (j * 10 + i) / (i * 10 + k) == j / k and 0 not in (k, i) and j != i:
                lcd.append(j / k)

# multiply our values together and flip the fraction
# 16/64, 26/65, 19/95, 49/98 -> 1/4, 2/5, 1/5, 1/2 -> 2/200 -> 1/100 -> ans: 100
print(functools.reduce(lambda x, y: x * y, lcd) ** (-1))  # 99.99999... -> 100
