# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

from primes import find_primes_less_than
from collections import deque
import bisect


def consecutive_prime_sum(p, greatest=1):
    consecutive_lst = deque(primes[:greatest])

    # we keep a running list of consecutive primes, when less than p, add the next prime, when greater drop the first
    for prime in primes[greatest:]:
        consecutive_lst.append(prime)

        while sum(consecutive_lst) > p:
            # if our smallest value times our longest length is greater than p, we know the length of p must be shorter
            if consecutive_lst.popleft() >= p // greatest:
                # we no longer care what value is returned as long as it is less than greatest
                return 1

        # the first time our list sums to p, return, as this is the longest the sum could be
        if sum(consecutive_lst) == p:
            return len(consecutive_lst)

    return 1  # our consecutive sum is only p


max_val = 10 ** 6
primes = find_primes_less_than(max_val)

longest = 0
longest_len = 1

# rough estimate that our solution is between 950000 and 1000000
for i in primes[bisect.bisect_left(primes, max_val // 100 * 95):]:
    p_sum = consecutive_prime_sum(i, longest_len)

    if p_sum > longest_len:
        longest_len, longest = p_sum, i

print(longest)  # 997651, p_sum == 543
