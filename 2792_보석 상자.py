import sys
from math import ceil
input = sys.stdin.readline

n, m = map(int, input().split())
jewels = [int(input()) for _ in range(m)]

result, left, right = 0, 1, max(jewels)
while left <= right:
    mid, cnt = (left + right) // 2, 0
    for jewel in jewels:
        cnt += ceil(jewel / mid)
    if cnt <= n:
        right = mid - 1
        result = mid
    else:
        left = mid + 1

print(result)