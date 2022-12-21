import sys
input = sys.stdin.readline

n = int(input())
prices = [list(map(int, input().split())) for _ in range(n)]
mapp = [[0] * n for _ in range(n)]
result = 20000


def count_price(row, price, cnt):
    if cnt == 3:
        global result
        result = min(result, price)
        return

    for i in range(row, n - 1):
        for j in range(1, n - 1):
            if mapp[i][j] != 1 and mapp[i - 1][j] != 1 and mapp[i + 1][j] != 1 and mapp[i][j - 1] != 1 and mapp[i][j + 1] != 1:
                mapp[i][j], mapp[i - 1][j], mapp[i + 1][j], mapp[i][j - 1], mapp[i][j + 1] = 1, 1, 1, 1, 1
                price2 = price
                price2 += prices[i][j] + prices[i - 1][j] + prices[i + 1][j] + prices[i][j - 1] + prices[i][j + 1]
                count_price(i, price2, cnt + 1)
                mapp[i][j], mapp[i - 1][j], mapp[i + 1][j], mapp[i][j - 1], mapp[i][j + 1] = 0, 0, 0, 0, 0


count_price(1, 0, 0)
print(result)