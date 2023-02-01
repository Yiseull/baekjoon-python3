import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)


def bfs(start):
    global result
    visited[start] = 0
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if visited[w] == -1:
                visited[w] = visited[v] + 1
                if visited[w] == k:
                    result.append(w)
                elif visited[w] > k:
                    break
                queue.append(w)


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [-1] * (n + 1)
result = []
bfs(x)
if result:
    result.sort()
    print('\n'.join(map(str, result)))
else:
    print(-1)