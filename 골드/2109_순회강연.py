import sys
import heapq
input = sys.stdin.readline

n = int(input())
pd = [list(map(int, input().split())) for _ in range(n)]
pd.sort(key=lambda x: (x[1], -x[0]))
heap = []
for p, d in pd:
    if d > len(heap):
        heapq.heappush(heap, p)
    elif heap[0] < p:
        heapq.heappop(heap)
        heapq.heappush(heap, p)
print(sum(heap))