# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ... , n) where n > 1?

from pandigital import is_pandigital

largest_pandigital = 0
# The largest number with pandigital potential that can be multiplied to a total of nine digits
# one of the given numbers starts with 9, so we must limit ourselves to start with numbers that start with 9
for i in range(9876, 8, -1):
    lp = str(i)
    if '0' in str(i):  # if 0 is in the number it does not fit the given definition of pandigital
        continue
    for n in range(2, 6):  # our largest n is 5, as shown in the example
        lp += str(i * n)
        if len(lp) >= 9:
            break
    if is_pandigital(lp) and int(lp) > largest_pandigital:
        largest_pandigital = int(lp)

print(largest_pandigital)  # 932718654
