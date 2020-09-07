# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

self_powers = set()
for i in range(1, 1000):
    self_powers.add(i ** i)  # brute force

print(str(sum(self_powers))[-10:])  # 9110846700
