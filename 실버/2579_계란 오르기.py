import sys
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    stairs = [0] * 301
    dp = [0] * 301
    for i in range(n):
        stairs[i] = int(input())

    dp[1], dp[2] = stairs[0], stairs[0] + stairs[1]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + stairs[i - 2], dp[i - 2]) + stairs[i - 1]

    print(dp[n])


main()
