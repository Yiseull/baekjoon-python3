def solution():
    dp[3], dp[5] = 1, 1
    for i in range(5, n + 1):
        if dp[i - 5] != 0:
            dp[i] = dp[i - 5] + 1
        elif dp[i - 3] != 0:
            dp[i] = dp[i - 3] + 1

n = int(input())

dp = [0] * (n + 1)

if n >= 5:
    solution()

if dp[n] == 0:
    print(-1)
else:
    print(dp[n])