import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
heap = []
for deadline, ramen in sorted(info, key=lambda x: x[0]):
    if deadline > len(heap):
        heappush(heap, ramen)
    elif heap[0] < ramen:
        heappop(heap)
        heappush(heap, ramen)

print(sum(heap))