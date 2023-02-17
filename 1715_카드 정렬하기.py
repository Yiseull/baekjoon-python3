import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
card = [int(input()) for _ in range(n)]
heapify(card)
result = 0
while len(card) != 1:
    a = heappop(card)
    b = heappop(card)
    cnt = a + b
    result += cnt
    heappush(card, cnt)
print(result)