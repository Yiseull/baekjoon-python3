import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
mapp = [input().strip() for _ in range(row)]
result = 0


def bfs(i, j):
    visited = [[-1] * col for _ in range(row)]
    visited[i][j] = 0
    queue = deque()
    queue.append([i, j])
    global result
    while queue:
        y, x = queue.popleft()
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < col and 0 <= next_y < row and mapp[next_y][next_x] == 'L' and visited[next_y][next_x] == -1:
                visited[next_y][next_x] = visited[y][x] + 1
                queue.append([next_y, next_x])
                result = max(result, visited[next_y][next_x])


for r in range(row):
    for c in range(col):
        if mapp[r][c] == 'L':
            bfs(r, c)

print(result)