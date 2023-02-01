import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        for w in pair[v]:
            if visited[w] == -1:
                visited[w] = visited[v] + 1
                if w == b:
                    return visited[w]
                q.append(w)
    return -1


a, b = map(int, input().split())
n, m = map(int, input().split())
pair = [[] for _ in range(n + 1)]
for _ in range(m):
    c, d = map(int, input().split())
    pair[c].append(d)
    pair[d].append(c)

if a == b:
    print(0)
else:
    print(bfs(a))