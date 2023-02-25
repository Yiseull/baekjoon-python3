import sys
from heapq import *
input = sys.stdin.readline


def dijkstra():
    visited = [[600] * m for _ in range(n)]
    visited[x1][y1] = 0
    q = []
    heappush(q, (0, x1, y1))
    while q:
        dist, x, y = heappop(q)
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < n and 0 <= next_y < m:
                if next_x == x2 and next_y == y2:
                    return visited[x][y] + 1
                if room[next_x][next_y] == '1':
                    cost = visited[x][y] + 1
                elif room[next_x][next_y] == '0':
                    cost = visited[x][y]
                if cost < visited[next_x][next_y]:
                    visited[next_x][next_y] = cost
                    heappush(q, (cost, next_x, next_y))


n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
room = [input().rstrip() for _ in range(n)]
print(dijkstra())