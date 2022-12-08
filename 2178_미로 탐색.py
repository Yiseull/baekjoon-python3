from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [input().strip() for _ in range(n)]


def bfs(i, j):
    cnt = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    visited[i][j] = True
    queue = deque()
    queue.append([i, j])
    while queue:
        li = queue.popleft()
        x, y = li[1], li[0]
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]
            if 0 <= next_x < m and 0 <= next_y < n and map[next_y][next_x] == '1' and not visited[next_y][next_x]:
                cnt[next_y][next_x] = cnt[y][x] + 1
                visited[next_y][next_x] = True
                queue.append([next_y, next_x])

    return cnt[n - 1][m - 1] + 1


print(bfs(0, 0))