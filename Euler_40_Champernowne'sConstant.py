# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

champernowne = ""

for i in range(1, 1000001):
    champernowne += str(i)

digit_multiple = 1

for i in range(7):  # counting starts at 0, so need 10^n - 1
    digit_multiple *= int(champernowne[10 ** i - 1])

print(digit_multiple)  # 210
