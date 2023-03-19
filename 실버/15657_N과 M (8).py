import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
print('\n'.join(list(map(' '.join, combinations_with_replacement(map(str, nums), m)))))
