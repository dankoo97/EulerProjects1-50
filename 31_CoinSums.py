# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
# 
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
# 
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


british_coins = [1, 2, 5, 10, 20, 50, 100, 200]  # coin values are in pence


# recursively finds how many different patterns of coins fit in a total x
def find_diff_sums(x, coin_values):
    if len(coin_values) == 1:  # with only one coin value left, there is only one possible way to reach the sum
        return 1

    n = 0

    for i in coin_values:
        if i > x:  # if our values are more than the total, we stop looking
            return n
        elif i == x:  # if our value is equal to the total, add it and stop looking
            n += 1
            return n
        else:
            # if our value is less than our total, find how many coins could go in the remaining total
            # we only use the current value or less so as not to repeat patterns
            n += find_diff_sums(x - i, coin_values[:coin_values.index(i) + 1])
    return n


print(find_diff_sums(200, british_coins))  # 73682
