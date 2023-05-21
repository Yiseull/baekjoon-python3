import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, distance, graph):
    q = [(0, start)]
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m, x = map(int, input().split())
distance1 = [INF] * (n + 1)
distance2 = [INF] * (n + 1)
graph1 = [[] for _ in range(n + 1)]
graph2 = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph1[a].append((b, t))
    graph2[b].append((a, t))

dijkstra(x, distance1, graph1)
dijkstra(x, distance2, graph2)

print(max(distance1[i] + distance2[i] for i in range(1, n + 1)))