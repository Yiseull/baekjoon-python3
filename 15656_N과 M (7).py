import sys
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
print('\n'.join(list(map(' '.join, product(map(str, nums), repeat=m)))))
