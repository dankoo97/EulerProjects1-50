# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from pandigital import is_pandigital

def is_mmp_pandigital(multiplicand, multiplier):
    product = multiplicand * multiplier
    return is_n_pandigital(str(multiplicand) + str(multiplier) + str(product))


MMPPandigital = set()  # use set to ignore duplicates


# a 1 digit number and a 4 digit number usually creates a 4 digit number giving us 9 total digits
# we skip 1 and 1000-1233 and 4988-9999 because:
# all of those numbers have repeated digits
# or 0 in them
# or will return a number with those conditions
# or will end with the incorrect number of digits for our entire iteration
for i in range(2, 10):
    for j in range(1234, 4988):  # 5000 == 10000 // 2... get rid of 0s and repeated digits -> 4987
        if is_mmp_pandigital(i, j):
            MMPPandigital.add(i * j)

# a 2 digit number and a 3 digit number usually creates a 4 digit number giving us 9 total digits
# we skip many numbers again for similar reasons as before
for i in range(12, 99):
    for j in range(123, 833):  # 832 == 10000 // 12
        if is_mmp_pandigital(i, j):
            MMPPandigital.add(i * j)

print(sum(MMPPandigital))  # 45228
