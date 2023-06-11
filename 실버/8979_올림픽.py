import sys
input = sys.stdin.readline


n, k = map(int, input().split())
medal = [tuple(map(int, input().split())) for _ in range(n)]
medal.sort(key=lambda x: (-x[1], -x[2], -x[3]))
rank = 1
if medal[0][0] == k:
    print(rank)
for i in range(1, n):
    if medal[i - 1][1] == medal[i][1] and medal[i - 1][2] == medal[i][2] and medal[i - 1][3] == medal[i][3]:
        pass
    else:
        rank = i + 1
    if medal[i][0] == k:
        print(rank)