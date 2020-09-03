fibonacci = [0, 1]

while len(str(fibonacci[-1])) < 1000:  # Brute force works quickly enough
    fibonacci += [fibonacci[-1] + fibonacci[-2]]

# print(fibonacci[-1])
# print()
print(len(fibonacci)-1)  # 4782
