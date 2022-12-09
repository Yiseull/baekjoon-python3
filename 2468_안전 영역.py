from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j):
    visited[i][j] = True
    queue = deque()
    queue.append([i, j])
    while queue:
        y, x = queue.popleft()
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < n and 0 <= next_y < n and graph[next_y][next_x] > rain and not visited[next_y][next_x]:
                visited[next_y][next_x] = True
                queue.append([next_y, next_x])


n = int(input())
graph = []
min_rain, max_rain = 100, 1
for _ in range(n):
    array = list(map(int, input().split()))
    min_rain = min(min_rain, min(array))
    max_rain = max(max_rain, max(array))
    graph.append(array)

result = 0
for rain in range(min_rain - 1, max_rain):  # range가 min_rain - 1부터 시작하는 이유: 아무 지역도 물에 잠기지 않을 수도 있다.
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > rain and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    result = max(result, cnt)

print(result)