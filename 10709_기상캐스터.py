import sys
input = sys.stdin.readline

h, w = map(int, input().split())
region = [input().strip() for _ in range(h)]

result = [[-1] * w for _ in range(h)]
for i, row in enumerate(region):
    for j, can in enumerate(row):
        if can == 'c':
            result[i][j] = 0
        else:
            if result[i][j-1] != -1 and result[i][j] != 0:
                result[i][j] = result[i][j-1] + 1

for row in result:
    for can in row:
        print(can, end=' ')
    print()