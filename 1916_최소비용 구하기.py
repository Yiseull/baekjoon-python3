import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
costs = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start_node, end_node = map(int, input().split())


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    costs[start] = 0
    while q:
        cost, node = heappop(q)
        if costs[node] < cost:
            continue
        for next_cost, next_node in graph[node]:
            val = costs[node] + next_cost
            if val < costs[next_node]:
                costs[next_node] = val
                heappush(q, (val, next_node))


dijkstra(start_node)
print(costs[end_node])