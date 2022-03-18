import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    # 시작 노드까지의 최단 경로를 0으로 설정하고, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 큐가 빌 때까지
    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리된 노드 무시
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 가는 경로가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 정점의 개수 V, 간선의 개수 E 입력
V, E = map(int, input().split())
# 시작 정점 K
k = int(input())

# 최단 거리 테이블 INF로 초기화
distance = [INF] * (V + 1)
# 방향그래프 정보를 담는 리스트
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    # u에서 v로 가는 가중치 w
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라 수행
dijkstra(k)

# 각 정점으로의 최단 경로값 출력
for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])