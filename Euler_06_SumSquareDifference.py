# The sum of the squares of the first ten natural numbers is, 385
# The square of the sum of the first ten natural numbers is, 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is . 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def square_of_sums(x):
    n = 0
    for i in range(x + 1):
        n += i
    return n ** 2


def sum_of_squares(x):
    n = 0
    for i in range(x + 1):
        n += i ** 2
    return n


print(square_of_sums(100) - sum_of_squares(100))  # 25164150
