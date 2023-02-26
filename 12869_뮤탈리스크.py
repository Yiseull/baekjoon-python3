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
        dp[0][0][0] = min(dp[0][0][0], cnt)
        return
    attack(scv1 - 9, scv2 - 3, scv3 - 1, cnt + 1)
    attack(scv1 - 9, scv2 - 1, scv3 - 3, cnt + 1)
    attack(scv1 - 3, scv2 - 9, scv3 - 1, cnt + 1)
    attack(scv1 - 3, scv2 - 1, scv3 - 9, cnt + 1)
    attack(scv1 - 1, scv2 - 9, scv3 - 3, cnt + 1)
    attack(scv1 - 1, scv2 - 3, scv3 - 9, cnt + 1)


n = int(input())
scv = list(map(int, input().split()))
dp = [[[14 for _ in range(61)] for _ in range(61)] for _ in range(61)]
if n == 1:
    print(ceil(scv[-1] / 9))
elif n == 2:
    attack(scv[0], scv[1], 0, 0)
    print(dp[0][0][0])
else:
    attack(scv[0], scv[1], scv[2], 0)
    print(dp[0][0][0])