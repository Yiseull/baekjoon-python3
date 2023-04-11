import sys
input = sys.stdin.readline


def solution() -> None:
    T, W = map(int, input().split())
    trees = [int(input()) for _ in range(T)]
    # 초 | 나무 번호 | 움직인 횟수
    dp = [[[0 for _ in range(W + 1)] for _ in range(2)] for _ in range(T + 1)]
    for t in range(1, T + 1):
        for w in range(W + 1):
            if trees[t - 1] == 1:
                if w == 0:
                    dp[t][0][0] = dp[t - 1][0][0] + 1
                else:
                    dp[t][0][w] = max(dp[t - 1][0][w], dp[t - 1][1][w - 1]) + 1
                    dp[t][1][w] = max(dp[t - 1][0][w - 1], dp[t - 1][1][w])
            else:
                if w == 0:
                    continue
                else:
                    dp[t][0][w] = max(dp[t - 1][0][w], dp[t - 1][1][w - 1])
                    dp[t][1][w] = max(dp[t - 1][0][w - 1], dp[t - 1][1][w]) + 1

    print(max(dp[T][0][W], dp[T][1][W]))


solution()
