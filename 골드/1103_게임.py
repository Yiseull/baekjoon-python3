import sys
input = sys.stdin.readline


def dfs(x, y) -> int:
    if dp[x][y] != -1:
        return dp[x][y]

    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        X = int(mapp[x][y])
        next_x = x + (dx * X)
        next_y = y + (dy * X)
        if 0 <= next_x < n and 0 <= next_y < m and mapp[next_x][next_y] != 'H':
            if visited[next_x][next_y]:
                print(-1)
                exit()

            visited[next_x][next_y] = True
            dp[x][y] = max(dp[x][y], dfs(next_x, next_y) + 1)
            visited[next_x][next_y] = False
        else:
            dp[x][y] = max(dp[x][y], 1)

    return dp[x][y]


if __name__ == '__main__':
    n, m = map(int, input().split())
    mapp = [list(input().strip()) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    dp = [[-1] * m for _ in range(n)]
    print(dfs(0, 0))
