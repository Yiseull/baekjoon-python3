import sys
input = sys.stdin.readline


def solution() -> None:
    T, W = map(int, input().split())
    trees = [int(input()) for _ in range(T)]
    dp = [[0 for _ in range(W + 1)] for _ in range(2)]
    for t in range(1, T + 1):
        for w in range(W + 1):
            if trees[t - 1] == 1:
                if w == 0:
                    dp[0][0] += 1
                else:
                    dp[0][w] = max(dp[0][w], dp[1][w - 1]) + 1
                    dp[1][w] = max(dp[0][w - 1], dp[1][w])
            else:
                if w == 0:
                    continue
                else:
                    dp[0][w] = max(dp[0][w], dp[1][w - 1])
                    dp[1][w] = max(dp[0][w - 1], dp[1][w]) + 1

    print(max(dp[0][W], dp[1][W]))


solution()
