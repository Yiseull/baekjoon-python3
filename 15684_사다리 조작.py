import sys
input = sys.stdin.readline


def check_ladder():
    for start in range(n):
        i, j = start, 0
        while j < h:
            if line[j][i] == 1:
                i += 1
            elif i > 0 and line[j][i - 1]:
                i -= 1
            j += 1
        if start != i:
            return False
    return True


def fix_ladder(i, j, cnt):
    if i < 0 or i >= n or j < 0 or j >= h:
        return

    global result
    if cnt > 3 or cnt >= result:
        return

    if check_ladder():
        result = min(result, cnt)
        return

    for ver in range(i, n - 1):
        for hor in range(j, h):
            if line[hor][ver] or line[hor][ver - 1] or (ver < n - 1 and line[hor][ver + 1]):
                continue
            line[hor][ver] = 1
            fix_ladder(ver, hor, cnt + 1)
            line[hor][ver] = 0
        j = 0


n, m, h = map(int, input().split())
line = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    line[a - 1][b - 1] = 1
result = 4
fix_ladder(0, 0, 0)
print(-1 if result > 3 else result)