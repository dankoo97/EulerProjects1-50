# 2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2 ** 1000?

print(sum(list(int(digit) for digit in str(2 ** 1000))))  # 1366

# We sum all of the digits. Python does this quick and easy, no tricks needed
