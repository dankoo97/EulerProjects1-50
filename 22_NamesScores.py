# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

from string import ascii_uppercase

with open('names.txt') as name_file:
    names = []
    for i in name_file:
        i = i.strip()
        names += i.split('"')

# preparing our list, there are extra chars, and it needs to be alphabetically sorted
names = list(filter(lambda a: a not in ('","', '"', ',', ''), names))
names.sort()

totalSum = 0

for i, name in enumerate(names, 1):
    name_sum = len(name)  # since the index starts at 0 we add one for each char, this is functionally the same
    for j in name:
        name_sum += ascii_uppercase.index(j)
    totalSum += (name_sum * i)

print(totalSum)  # 871198282
