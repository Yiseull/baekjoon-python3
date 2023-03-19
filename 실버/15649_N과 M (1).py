import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [str(i) for i in range(1, n + 1)]
pers = list(permutations(nums, m))
print('\n'.join(' '.join(per) for per in pers))