import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def dijkstra(min, max):
    global time, ways
    q = deque([n])
    visited = defaultdict(int)
    visited[n] = 0
    cnt = 0
    while q:
        x = q.popleft()
        cnt = visited[x] + 1
        if time < cnt:
            return
        for v in [x - 1, x + 1, x * 2]:
            if min < v < max and (v not in visited or visited[v] == cnt):
                if v == k:
                    time = cnt
                    ways += 1
                else:
                    q.append(v)
                    visited[v] = cnt


n, k = map(int, input().split())
time, ways = abs(n - k) + 1, 0
if n < k:
    dijkstra(max(0, n - time), k + time)
    print(time)
    print(ways)
else:
    print(n - k)
    print(1)