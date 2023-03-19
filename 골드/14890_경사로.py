import sys
input = sys.stdin.readline


def find_way(way):
    cnt = 1
    for i, h in enumerate(way[1:]):
        if h == way[i]:
            cnt += 1
        elif h == way[i] + 1 and cnt >= l:
            cnt = 1
        elif h == way[i] - 1 and cnt >= 0:
            cnt = -l + 1
        else:
            return 0
    if cnt < 0:
        return 0
    return 1


n, l = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
print(sum(find_way(i) for i in mapp) + sum(find_way(i) for i in zip(*mapp)))