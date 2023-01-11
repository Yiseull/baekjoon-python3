import sys
from math import ceil
input = sys.stdin.readline

n, atk = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
hp, max_hp = 0, 0
for t, a, h in info:
    if t == 1:
        hp += (ceil(h / atk) - 1) * a
    else:
        max_hp = max(max_hp, hp)
        atk += a
        hp -= h
        if hp < 0:
            hp = 0

print(max(max_hp, hp) + 1)