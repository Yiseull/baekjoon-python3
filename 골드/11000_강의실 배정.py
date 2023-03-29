import sys
from heapq import *
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    lectures = [list(map(int, input().split())) for _ in range(n)]
    lectures.sort(key=lambda x: x[0])

    heap, cnt = [], 0
    for s, t in lectures:
        if heap and heap[0] <= s:
            heapreplace(heap, t)
        else:
            cnt += 1
            heappush(heap, t)

    print(cnt)


main()