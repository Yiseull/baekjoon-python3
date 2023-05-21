import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
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
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
answer = 0

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))

dijkstra(x, distance)

for i in range(1, n + 1):
    if i == x:
        continue
    distance2 = [INF] * (n + 1)
    dijkstra(i, distance2)
    answer = max(answer, distance[i] + distance2[x])

print(answer)