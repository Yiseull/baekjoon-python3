import sys
input = sys.stdin.readline

n, k = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
wv.sort()
dp = [0] * (k + 1)
for w, v in wv:
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i - w] + v, dp[i])
print(dp[k])