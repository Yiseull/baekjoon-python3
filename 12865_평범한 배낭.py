import sys
input = sys.stdin.readline

n, k = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n)]
for i in range(n):
    for w in range(1, k + 1):
        if wv[i][0] > w:
            dp[i][w] = dp[i - 1][w]
        else:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wv[i][0]] + wv[i][1])
print(dp[n - 1][w])