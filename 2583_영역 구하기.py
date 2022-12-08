from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j):
    graph[i][j] = 0
    queue = deque()
    queue.append([i, j])
    area = 0
    while queue:
        li = queue.popleft()
        x, y = li[1], li[0]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]
            if 0 <= next_x < n and 0 <= next_y < m and graph[next_y][next_x] == 1:
                graph[next_y][next_x] = 0
                queue.append([next_y, next_x])
                area += 1

    return area


m, n, k = map(int, input().split())
graph = [[1] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 0

cnt = 0
area = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            area.append(bfs(i, j) + 1)
            cnt += 1

print(cnt)
for a in sorted(area):
    print(a, end=' ')