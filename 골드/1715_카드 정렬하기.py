from heapq import *

n, *card = map(int, open(0))
heapify(card)
result = 0
for _ in range(n - 1):
    cnt = heappop(card) + heappop(card)
    result += cnt
    heappush(card, cnt)
print(result)