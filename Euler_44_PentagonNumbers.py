# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk,
# for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised;
# what is the value of D?


# given formula
def pent(n):
    return (3 * n ** 2 - n) // 2


# checks if Pn is a pentagonal number
def is_pent(Pn):
    return ((1 + 24 * Pn) ** 0.5) % 6 == 5


n = 1
while True:
    Pk = pent(n)
    for j in range(1, n):  # check each number below our nth number to see if it fits for j
        Pj = pent(j)
        if is_pent(Pk - Pj) and is_pent(Pk + Pj):
            print(Pk - Pj)  # D == 5482660
            break
    else:
        n += 1
        continue
    break