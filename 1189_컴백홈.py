import sys
from copy import deepcopy
input = sys.stdin.readline

r, c, k = map(int, input().split())
mapp = [input().strip() for _ in range(r)]
result = 0


def dfs(x, y, cnt, visited):
    if x == c - 1 and y == 0:
        if cnt == k:
            global result
            result += 1
        return

    visited[y][x] = True
    new_visited = deepcopy(visited)
    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        next_x = x + dx
        next_y = y + dy
        if 0 <= next_x < c and 0 <= next_y < r and mapp[next_y][next_x] == '.' and not new_visited[next_y][next_x]:
            new_visited[next_y][next_x] = True
            dfs(next_x, next_y, cnt + 1, new_visited)
            new_visited[next_y][next_x] = False


dfs(0, r - 1, 1, [[False for _ in range(c)] for _ in range(r)])
print(result)