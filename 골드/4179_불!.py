import sys
from collections import deque
input = sys.stdin.readline


def fire(i, j):
    visited[i][j] = 0
    queue = deque()
    queue.append([i, j])
    while queue:
        y, x = queue.popleft()
        time = visited[y][x] + 1
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < c and 0 <= next_y < r and miro[next_y][next_x] != '#' and time < visited[next_y][next_x]:
                visited[next_y][next_x] = time
                queue.append([next_y, next_x])


def escape(i, j):
    visited[i][j] = 0
    queue = deque()
    queue.append([i, j])
    while queue:
        y, x = queue.popleft()
        time = visited[y][x] + 1
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < c and 0 <= next_y < r and miro[next_y][next_x] != '#' and time < visited[next_y][next_x]:
                if next_x == 0 or next_x == c - 1 or next_y == 0 or next_y == r - 1:
                    return time + 1
                visited[next_y][next_x] = time
                queue.append([next_y, next_x])
    return 'IMPOSSIBLE'


r, c = map(int, input().split())
miro = [list(input().rstrip()) for _ in range(r)]
visited = [[2000] * c for _ in range(r)]
jx, jy = 0, 0
for i in range(r):
    for j in range(c):
        if miro[i][j] == 'F':
            fire(i, j)
        elif miro[i][j] == 'J':
            jy, jx = i, j
if jx == 0 or jx == c - 1 or jy == 0 or jy == r - 1:
    print(1)
else:
    print(escape(jy, jx))