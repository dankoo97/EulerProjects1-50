# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def create_path(x):
    try:
        if chains[x] in chains:  # We check our dict if we already found the length of x
            return chains[x]
    except KeyError:
        pass

    if x % 2 == 0:
        chains[x] = 1 + create_path(x // 2)  # Even collatz
        return chains[x]

    i = 1
    while (x + 1) * 2 ** -i % 2 == 0:  # Since an odd number will always be followed by an even, we can skip that step
        i += 1                         # This is a more advanced formula that will try to catch a train of these in a row
                                       # to reduce the number of recursions

    y = int((x + 1) * (3 / 2) ** i) - 1

    chains[x] = 2 * i + create_path(y)
    return chains[x]


chains = {1: 0, 2: 1}  # our base collatz used for recursion

collatz_range = 1000000  # given range

longest = 0  # initial comparisons
length = 0

for num in range(collatz_range // 2, collatz_range):

    n = create_path(num)

    if n > length:
        longest, length = num, n

print(longest)  # 837799
print(length)   # 524
