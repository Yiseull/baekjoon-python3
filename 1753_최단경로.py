import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())
graph = [dict() for _ in range(v + 1)]
distance = [INF] * (v + 1)
for _ in range(e):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heappop(q)
        if distance[node] < dist:
            continue
        for next_node, next_cost in graph[node].items():
            cost = distance[node] + next_cost
            if cost < distance[next_node]:
                distance[next_node] = cost
                heappush(q, (cost, next_node))


dijkstra(k)
for dist in distance[1:]:
    print('INF' if dist == INF else dist)