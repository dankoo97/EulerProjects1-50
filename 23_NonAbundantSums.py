# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

abundant_numbers = set()
max_int = 28124
possible_sums = [True] * max_int  # We create a boolean array to mark whether a number is an abundant sum or not


def is_abundant_number(n):
    factors = {1, }
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)  # since our numbers are relatively small we can use an inefficient algorithm to calculate our factors
    return sum(factors) > n


for num in range(10, max_int):
    if possible_sums[num]:
        if is_abundant_number(num):
            abundant_numbers.add(num)
            for multiple in range(num * 2, max_int, num):  # if a number is an abundant number all multiples of that number are also abundant
                possible_sums[multiple] = False            # we use a set to eliminate duplicates
                abundant_numbers.add(multiple)

abundant_numbers = list(abundant_numbers)  # we turn our set into a sorted list so that we can find more efficiently find all sums
abundant_numbers.sort()                    # we sort here so that we only need to sort once

for index, bottom_num in enumerate(abundant_numbers):
    for top_num in abundant_numbers[index + 1:]:
        if top_num + bottom_num >= max_int:
            break
        possible_sums[bottom_num + top_num] = False  # marking sums

sums = [i for i in range(1, max_int) if possible_sums[i]]  # turning our bool list into numbers
# print(*sums, sep='\n')
print(sum(sums))  # 4179871
