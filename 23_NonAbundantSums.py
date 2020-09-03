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
