from collections import deque

# 깊이 우선 탐색 DFS
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    # 정점 번호가 작은 것부터 방문
    list = graph[start]
    list.sort()
    for i in list:
        if visited[i] == False:
            dfs(graph, i, visited)


# 넓이 우선 탐색 BFS
def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    print(start, end=' ')
    # 큐가 빌 때까지
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                print(i, end=' ')


# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V 입력
n, m, v = map(int, input().split())

# 간선이 연결하는 두 정점의 번호
graph = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    # 간선은 양방향
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
# DFS 실행
dfs(graph, v, visited)

print(graph)

visited = [False] * (n + 1)
# BFS 실행
bfs(graph, v, visited)