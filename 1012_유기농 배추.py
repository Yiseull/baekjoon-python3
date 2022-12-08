from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j, table, visited):
    visited[i][j] = True
    queue = deque()
    queue.append([i, j])
    while queue:
        li = queue.popleft()
        x, y = li[1], li[0]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]
            if 0 <= next_x < m and 0 <= next_y < n and table[next_y][next_x] == 1 and not visited[next_y][next_x]:
                visited[next_y][next_x] = True
                queue.append([next_y, next_x])


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    table = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        table[y][x] = 1
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1 and not visited[i][j]:
                bfs(i, j, table, visited)
                cnt += 1
    print(cnt)