# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# 
# That is, 3 + 7 + 4 + 9 = 23.
# 
# Find the maximum total from top to bottom of the triangle below:
# 
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
# 
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
# it cannot be solved by brute force, and requires a clever method! ;o)

def path_sum(file_path):

    def get_greatest_sum(x=0, y=0):
        pos = (str(x) + ',' + str(y))
        if pos in sums:
            return sums[pos]  # prevent extra calculations

        l_sum = get_greatest_sum(x + 1, y)        # triangle is left adjusted, so going down the left path from the top is triangle[x][0]
        r_sum = get_greatest_sum(x + 1, y + 1)    # and the right path is triangle [x][len(triangle[x] - 1]

        sums[pos] = (l_sum if l_sum > r_sum else r_sum) + triangle[x][y]  # we compare the sum of the left path and right path, return the greater and add the val of our position

        return sums[pos]

    triangle = []
    with open(file_path) as tx:
        for i in tx:
            i = i.strip('\n')
            triangle += [i.split(' ')]

    for i in range(len(triangle)):
        triangle[i] = [int(j) for j in triangle[i]]  # turning our text into a 2d list of int

    sums = {}  # storing found sums for positions

    for j in range(len(triangle[-1])):
        sums[str(len(triangle) - 1) + ',' + str(j)] = triangle[-1][j]  # the bottom row is inputted into our sums so we have a base

    return get_greatest_sum()


def __main__():
    print(path_sum('triangle1.txt'))  # 1074


if __name__ == '__main__':  # we will use the same method for problem 67
    __main__()
