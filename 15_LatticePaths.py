# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

paths = {'2,2': 6}  # Cache for found paths


def lattice_path(x, y):
    for i in range(2):
        try:
            if str(x)+","+str(y) in paths:
                return paths[str(x) + ',' + str(y)]  # check if we already did the work for this size lattice
        except KeyError:
            x, y = y, x  # flip the digits because the outcome is the same and it halves the calculations

    if x == 1 or y == 1:
        paths[str(x) + ',' + str(y)] = x + y  # a 1xX lattice will always have X + 1 paths available
        return x + y

    else:
        paths[str(x) + ',' + str(y)] = lattice_path(x - 1, y) + lattice_path(x, y - 1)  # creates 2 unique paths and sums them
        return paths[str(x) + ',' + str(y)]


print(lattice_path(20, 20))  # 137846528820
