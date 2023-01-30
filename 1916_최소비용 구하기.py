import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [dict() for _ in range(n + 1)]
costs = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c
start_node, end_node = map(int, input().split())


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    costs[start] = 0
    while q:
        cost, node = heappop(q)
        if costs[node] < cost:
            continue
        for next_node, next_cost in graph[node].items():
            val = costs[node] + next_cost
            if val < costs[next_node]:
                costs[next_node] = val
                heappush(q, (val, next_node))


dijkstra(start_node)
print(costs[end_node])