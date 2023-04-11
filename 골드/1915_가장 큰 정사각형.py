import sys
input = sys.stdin.readline


def square(x, y, array, dp) -> int:
    length = dp[x - 1][y - 1]
    for i in range(1, length + 1):
        if array[x - i][y] != '1' or array[x][y - i] != '1':
            return i

    return length + 1


def main() -> None:
    n, m = map(int, input().split())
    array = [input().strip() for _ in range(n)]
    dp = [[-1] * m for _ in range(n)]
    max_length = 0

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = int(array[i][j])
            elif array[i][j] == '1':
                if array[i - 1][j - 1] == '1':
                    dp[i][j] = square(i, j, array, dp)
                else:
                    dp[i][j] = 1

            max_length = max(max_length, dp[i][j])

    print(max_length * max_length)


main()
