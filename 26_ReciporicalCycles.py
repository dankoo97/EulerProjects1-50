# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import time

import decimal
import re
from primes import find_primes_less_than

decimal.getcontext().prec = 3000  # this should be more than long enough for us to detect a cycle
decimal.getcontext().rounding = decimal.ROUND_DOWN
limit = 1000

# we skip 2, 3, 5 because we know that they terminate or have short cycles
# all other primes should have cycles of interest
primes = find_primes_less_than(limit)[3:]


def get_cycle_length(n):
    # get a sufficiently long and accurate decimal, remove the leading '0.0*'
    # this breaks on decimals that terminate quickly but we do not care to find those.
    dec_str = str(decimal.Decimal(1) / decimal.Decimal(n))[len(str(n)) + 1:]

    # at most, the cycle can be length n - 1
    for i in range(n - 1, 1, -1):
        regex = re.compile(dec_str[:i])
        if regex.match(dec_str[i: i * 2]) and regex.match(dec_str[i * 2: i * 3]):
            if dec_str[:i // 2] == dec_str[i // 2: i]:  # checks if the pattern is itself repeated within the regex
                continue
            return i

    return 0


longest_cycle = 1
longest_cycle_val = 3

start_time = time.time()
for prime in primes:
    if get_cycle_length(prime) > longest_cycle:
        longest_cycle = get_cycle_length(prime)
        longest_cycle_val = prime
print(time.time() - start_time)  # approx 30 sec

print('cycle val:     ' + str(longest_cycle_val))  # 983
print('cycle length:  ' + str(longest_cycle))      # 982
