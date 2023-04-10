import sys
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    amount = [int(input()) for _ in range(n)]
    if n < 3:
        print(sum(amount))
    else:
        dp = [0] * (n + 1)
        dp[1], dp[2] = amount[0], amount[0] + amount[1]
        for i in range(3, n + 1):
            dp[i] = max(dp[i - 2], dp[i - 3] + amount[i - 2]) + amount[i - 1]
            dp[i] = max(dp[i], dp[i - 1])

        print(dp[n])


main()