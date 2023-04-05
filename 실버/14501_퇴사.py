import sys
from heapq import *
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    scheduler = [list(map(int, input().split())) for _ in range(n)]

    heap1, heap2 = [], []
    for i, schedule in enumerate(scheduler):
        while heap1 and heap1[0][0] <= i:
            heappush(heap2, -heappop(heap1)[1])

        cost = schedule[1]
        if heap2:
            cost += -heap2[0]

        heappush(heap1, (i + schedule[0], cost))

    while heap1 and heap1[0][0] <= n:
        heappush(heap2, -heappop(heap1)[1])

    print(-heap2[0] if heap2 else 0)


main()
