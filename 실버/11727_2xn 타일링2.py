import sys
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    if n == 1:
        print(1)
    else:
        dp = [0] * n
        dp[0], dp[1] = 1, 3
        for i in range(2, n):
            dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007
        print(dp[n - 1])


main()
