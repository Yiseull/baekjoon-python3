import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
day = 0


def bfs(i, j):
    visited[i][j] = True
    queue = deque()
    queue.append([i, j])
    union = []
    total = 0
    while queue:
        y, x = queue.popleft()
        union.append([y, x])
        total += population[y][x]
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_y][next_x] and L <= abs(population[y][x] - population[next_y][next_x]) <= R:
                visited[next_y][next_x] = True
                queue.append([next_y, next_x])

    if len(union) > 1:
        avg = total // len(union)
        for row, col in union:
            population[row][col] = avg
        return True
    return False


while 1:
    visited = [[False] * N for _ in range(N)]
    occur = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and bfs(i, j):
                occur = True
    if not occur:
        break
    day += 1

print(day)
