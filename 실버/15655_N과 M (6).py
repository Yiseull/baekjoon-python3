import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
pers = list(combinations(nums, m))
print('\n'.join(' '.join(map(str, per)) for per in pers))
