import sys
from math import ceil
input = sys.stdin.readline


def attack(scv1, scv2, scv3, cnt):
    if scv1 < 0: scv1 = 0
    if scv2 < 0: scv2 = 0
    if scv3 < 0: scv3 = 0

    if dp[scv1][scv2][scv3] <= cnt:
        return
    dp[scv1][scv2][scv3] = cnt

    if scv1 == 0 and scv2 == 0 and scv3 == 0:
        return

    for a, b, c in [[9, 3, 1], [9, 1, 3], [3, 9, 1], [3, 1, 9], [1, 9, 3], [1, 3, 9]]:
        attack(scv1 - a, scv2 - b, scv3 - c, cnt + 1)


n = int(input())
scv = list(map(int, input().split()))
dp = [[[14 for _ in range(61)] for _ in range(61)] for _ in range(61)]
if n == 1:
    print(ceil(scv[-1] / 9))
else:
    while len(scv) < 3:
        scv.append(0)
    attack(scv[0], scv[1], scv[2], 0)
    print(dp[0][0][0])