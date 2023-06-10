import sys
input = sys.stdin.readline


n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
answer = [0] * n
for i in range(n):
    cnt = 0
    for j in range(n):
        if info[j][0] > info[i][0] and info[j][1] > info[i][1]:
            cnt += 1
    answer[i] = cnt + 1
print(' '.join(map(str, answer)))