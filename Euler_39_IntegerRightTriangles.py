# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

# We need to find pythagorean triples, here is a graphic representation of pythagorean triples
# https://upload.wikimedia.org/wikipedia/commons/c/cc/PrimitivePythagoreanTriplesRev08.svg


# smallest pythagorean triple is 3, 4, 5
# all pythagorean triples are even sums
perimeter_range = range(12, 1001, 2)


def perimeter_is_multiple_of_sum_of_sides(perimeter, sum_of_sides):
    # if the perimeter is a multiple of the sum of sides, than a multiple is a solution to the perimeter,
    # we do not need to find the solution, only know that it exists.
    # it is impossible for multiple solutions to exist with the same specific pythagorean triple
    return perimeter % sum_of_sides == 0


most_solutions = 0
most_solutions_value = 0

for p in perimeter_range:
    num_of_solutions = 0

    # pythagorean triples take the form of one side of a triangle
    # being a product of two odd numbers such that: |a - b| >= 2
    #
    # the other sides sum to the square of the greater of a and b: where a > b, a^2 == c + d
    # and also the difference between these two sides is equal to the value of the lesser odd: where a > b, |c - d| == b
    #
    # Therefore the sum of the sides == c + d + (a * b) == a^2 + (a*b)
    # ex. sum(3, 4, 5) == 12 == (3^2) + 3*1, sum(15, 8, 17) == 40 == (5^2) + 5*3, sum(21, 20, 29) == 70 == (7^2) + 7*3
    for side_a_mult in range(1, p // 2, 2):
        for side_a in range(side_a_mult + 2, p // 2, 2):

            # we break at p // 2 because no triangle can exist with one side
            # being greater than or equal to the sum of the other sides
            if side_a * side_a_mult >= p // 2:
                break

            if perimeter_is_multiple_of_sum_of_sides(p, side_a ** 2 + side_a_mult * side_a):
                num_of_solutions += 1

    if num_of_solutions > most_solutions_value:
        most_solutions = p
        most_solutions_value = num_of_solutions


print(most_solutions)  # 840
