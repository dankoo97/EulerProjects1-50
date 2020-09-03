# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

fifth_powers = set()

# brute forced, we only look for up to 6-digit numbers as (7 * 9^5) < (6 * 10^5)
for i in range(2, 1000000):
    if i == sum([int(j) ** 5 for j in str(i)]):
        fifth_powers.add(i)

print(sum(fifth_powers))  # 443839
