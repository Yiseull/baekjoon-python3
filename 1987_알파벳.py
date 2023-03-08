import sys
input = sys.stdin.readline


def dfs(x, y, cnt):
    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        next_x = x + dx
        next_y = y + dy
        if 0 <= next_x < c and 0 <= next_y < r and not visited[ord(board[next_y][next_x]) - 65]:
            visited[ord(board[next_y][next_x]) - 65] = True
            dfs(next_x, next_y, cnt + 1)
            visited[ord(board[next_y][next_x]) - 65] = False

    global result
    result = max(result, cnt)


r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]
visited = [0] * 26
visited[ord(board[0][0]) - 65] = True
result = 0
dfs(0, 0, 1)
print(result)