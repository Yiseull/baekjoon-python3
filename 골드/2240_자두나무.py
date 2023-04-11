import sys
input = sys.stdin.readline


def solution() -> None:
    t, w = map(int, input().split())
    trees = [int(input()) for _ in range(t)]
    dp = [[0 for _ in range(2)] for _ in range(w + 1)]

    for tree in trees:
        for i in range(w + 1):
            if tree == 1:
                if i == 0:
                    dp[0][0] += 1
                else:
                    dp[i][0] = max(dp[i][0], dp[i - 1][1]) + 1
                    dp[i][1] = max(dp[i - 1][0], dp[i][1])
            else:
                if i == 0:
                    continue
                else:
                    dp[i][0] = max(dp[i][0], dp[i - 1][1])
                    dp[i][1] = max(dp[i - 1][0], dp[i][1]) + 1

    print(max(dp[w]))


solution()
