import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(x, y) -> int:
    if visited[x][y]:
        print(-1)
        exit()

    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1

    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        X = int(mapp[x][y])
        next_x = x + (dx * X)
        next_y = y + (dy * X)
        if 0 <= next_x < n and 0 <= next_y < m and mapp[next_x][next_y] != 'H':
            visited[x][y] = True
            dp[x][y] = max(dp[x][y], dfs(next_x, next_y) + 1)
            visited[x][y] = False

    return dp[x][y]


if __name__ == '__main__':
    n, m = map(int, input().split())
    mapp = [list(input().strip()) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    print(dfs(0, 0))
