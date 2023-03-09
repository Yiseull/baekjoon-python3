import sys
input = sys.stdin.readline

n, l = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
result = 0
for i in range(n):
    way = True
    slope = mapp[i][0]
    j = 1
    s = set()
    while j < n:
        if slope != mapp[i][j]:
            if abs(slope - mapp[i][j]) > 1:
                way = False
            if slope > mapp[i][j]:
                if j + l > n:
                    way = False
                    break
                slope2 = mapp[i][j]
                for d in range(l):
                    if slope2 != mapp[i][j + d] or j + d in s:
                        way = False
                        break
                if not way:
                    break
                slope = mapp[i][j]
                for d in range(l):
                    s.add(j + d)
                j += l
                continue
            elif j >= l:
                for d in range(1, l + 1):
                    if slope != mapp[i][j - d] or j - d in s:
                        way = False
                        break
                if not way:
                    break
                slope = mapp[i][j]
                for d in range(1, l + 1):
                    s.add(j - d)
            else:
                way = False
                break
        j += 1
    if way:
        result += 1

    way = True
    slope = mapp[0][i]
    j = 1
    s = set()
    while j < n:
        if slope != mapp[j][i]:
            if abs(slope - mapp[j][i]) > 1:
                way = False
            if slope > mapp[j][i]:
                if j + l > n:
                    way = False
                    break
                slope2 = mapp[j][i]
                for d in range(l):
                    if slope2 != mapp[j + d][i] or j + d in s:
                        way = False
                        break
                if not way:
                    break
                slope = mapp[j][i]
                for d in range(l):
                    s.add(j + d)
                j += l
                continue
            elif j >= l:
                for d in range(1, l + 1):
                    if slope != mapp[j - d][i] or j - d in s:
                        way = False
                        break
                if not way:
                    break
                slope = mapp[j][i]
                for d in range(1, l + 1):
                    s.add(j - d)
            else:
                way = False
                break
        j += 1
    if way:
        result += 1

print(result)