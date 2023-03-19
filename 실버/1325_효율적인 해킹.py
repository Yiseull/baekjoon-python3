import sys
from collections import deque
input = sys.stdin.readline


def bfs(i):
    hacking = [False] * (n + 1)
    hacking[i] = True
    q = deque([i])
    while q:
        b = q.popleft()
        count[i] += 1
        for a in reliable[b]:
            if not hacking[a]:
                hacking[a] = True
                q.append(a)


n, m = map(int, input().split())
reliable = [[] for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    reliable[b].append(a)

count = [0] * (n + 1)
max = 0
result = []
for i, computers in enumerate(reliable):
    if computers:
        bfs(i)
        if count[i] > max:
            max = count[i]
            result = [i]
        elif count[i] == max:
            result.append(i)
print(' '.join(map(str, result)))