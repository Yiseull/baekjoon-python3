import sys
from math import ceil
input = sys.stdin.readline

n, power = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
left, right, result = 1, 123455876544000001, 123455876544000001
while left <= right:
    hp = mid = (left + right) // 2
    atk = power
    for t, a, h in info:
        if t == 1:
            cnt1, cnt2 = ceil(h / atk), ceil(hp / a)
            if cnt1 > cnt2:
                hp = -1
                break
            else:
                hp -= (cnt1 - 1) * a
        else:
            atk += a
            hp += h
            if hp > mid:
                hp = mid

    if hp > 0:
        right = mid - 1
        result = min(result, mid)
    else:
        left = mid + 1

print(result)