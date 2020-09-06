# The nth term of the sequence of triangle numbers is given by,
# tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position
# and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English words, how many are triangle words?
import string


# nothing the problem requires is the nth triangle sum, just that a word sum is a triangle sum
# so instead we create a list of all triangle sums less than or equal to our max word sum
def find_triangle_numbers_lte(n):
    tri = [1]
    while tri[-1] <= n:
        tri.append(tri[-1] + len(tri) + 1)
    return tri


word_values = []

with open('words.txt', 'r') as words:
    for word in words.read().split(','):  # turning our file into a list of word sums
        word_values.append(sum(string.ascii_uppercase.index(char) + 1 for char in word.strip('"')))


# we only need a list of triangle sums up to our max word sum
triangle_numbers = find_triangle_numbers_lte(max(word_values))


triangle_count = 0
for word_value in word_values:
    if word_value in triangle_numbers:
        triangle_count += 1

print(triangle_count)  # 162
