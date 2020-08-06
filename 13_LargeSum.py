# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# Big number was put in a text file for easier reading

with open("bigNum.txt") as big_num_file
    bigNum = []
    for i in big_num_file:
        bigNum += [str(i).strip("\n")]
    bigNum = [int(i) for i in bigNum]
print(str(sum(bigNum))[:10])  # 5537376230, python sums it pretty quick so no need for special algorithm
