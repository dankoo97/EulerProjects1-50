# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

limit = 1000000
palindromic_nums = set()  # using a set eliminates duplicates


def is_palindrome(n):
    for digit in range(len(str(n)) // 2):  # only need to go through the first half of the string for comparison and not check the middle
        if str(n)[digit] != str(n)[-digit - 1]:
            return False
    return True


for i in range(1, limit, 2):  # all even numbers end in 0 in binary and we cannot have leading 0s
    if is_palindrome(i) and is_palindrome(bin(i)[2:]):
        palindromic_nums.add(i)

print(sum(palindromic_nums))  # 872187
