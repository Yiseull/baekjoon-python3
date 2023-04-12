import sys
input = sys.stdin.readline


def main() -> None:
    n, m = map(int, input().split())
    array = [input().strip() for _ in range(n)]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if array[i - 1][j - 1] == '1':
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

    max_length = max(map(max, dp))
    print(max_length ** 2)


main()
