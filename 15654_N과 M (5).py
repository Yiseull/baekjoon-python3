import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
pers = list(permutations(nums, m))
print('\n'.join(' '.join(map(str, per)) for per in pers))
