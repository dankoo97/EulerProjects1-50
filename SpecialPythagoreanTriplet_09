# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# See https://en.wikipedia.org/wiki/Pythagorean_triple#/media/File:PrimitivePythagoreanTriplesRev08.svg for a chart of pythagorean triples
# Pythagorean triples are right triangles where each of the sides is a natural number
def pythagorean_triple_sum(x):
    init = [1, 3]
    # The only numbers needed to generate a pythagorean triple,
    # one side of the triangle is always the product of these numbers,
    # the other sides sum to the square of init[1]

    while init[1] <= x // 2:  # One side of a triangle cannot be more than the sum of the other two sides, therefore we know if one side is greater than half our sum we cannot make a triangle
        if x % ((init[0] * 2 - 1) * init[1] + init[1] ** 2) == 0:  # checks the sum of all the sides using the only numbers needed

            multi = x // ((init[0] * 2 - 1) * init[1] + init[1] ** 2)  # pythagorean triples can be multiplied by a constant to get a related pythagorean triple

            return (
                ((init[0] * 2 - 1) * init[1]) * multi,  # a side is given by multiplying two odd numbers
                sum(4 * x for x in range(init[0], (init[1] + 1) // 2)) * multi,  # b side is a sum of a series of multiples of four
                ((init[1]) ** 2 - sum(4 * x for x in range(init[0], (init[1] + 1) // 2))) * multi  # in a pythagorean triple c = init[1] ** 2 - b
            )

        init[1] += 2

        if init[1] >= x // 3:
            init[0] += 1
            init[1] = init[0] * 2 + 1

    return False


py_trip_1000 = pythagorean_triple_sum(1000)

print(py_trip_1000)  # (375, 200, 425)
print(py_trip_1000[0] * py_trip_1000[1] * py_trip_1000[2])  # 31875000
