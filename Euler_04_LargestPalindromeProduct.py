# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome(digits):
    x = [10 ** (digits - 1), 10 ** (digits - 1), 10 ** digits]  # Base case
    lim = [10 ** (digits - 1), (10 ** digits) - 1]

    while lim[0] != lim[1] and lim[1] ** 2 > x[2]:  # Keeps moving while it is worthwhile to check
        for i in range(lim[1], lim[0], -1):
            if is_palindrome(i*lim[1]) and i*lim[1] > x[2]:
                x[0] = i
                x[1] = lim[1]
                x[2] = x[0] * x[1]
                break
            elif lim[1] * i < x[2]:
                break
        lim[1] -= 1  # Gradually decreases top number
    return x


def is_palindrome(x):
    x = str(x)
    for i in range(len(x) // 2):
        if x[i] != x[-i - 1]:
            return False
    return True


print(largest_palindrome(3))  # 906609
