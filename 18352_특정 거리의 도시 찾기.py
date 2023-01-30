import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for next_node in graph[now]:
            cost = distance[now] + 1
            if cost < distance[next_node]:
                distance[next_node] = cost
                heappush(q, (cost, next_node))


dijkstra(x)
result = ''
for i, dist in enumerate(distance):
    if dist == k:
        result += str(i) + '\n'
print(-1 if len(result) == 0 else result)