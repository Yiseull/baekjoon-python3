import sys
import heapq
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
info.sort(key=lambda x: (x[0], -x[1]))
heap = []
for deadline, ramen in info:
    if deadline > len(heap):
        heapq.heappush(heap, ramen)
    elif heap[0] < ramen:
        heapq.heappop(heap)
        heapq.heappush(heap, ramen)
print(sum(heap))