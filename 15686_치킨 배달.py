import sys
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
chicken, house = [], []
result = 2500

for i in range(n):
    li = list(map(int, input().split()))
    for j in range(len(li)):
        if li[j] == 1:
            house.append([i, j])
        elif li[j] == 2:
            chicken.append([i, j])


def chicken_street(cnt, distance, idx):
    global result
    if cnt == m:
        return

    for i in range(idx, len(chicken)):
        new_distance = deepcopy(distance)
        for j in range(len(house)):
            new_distance[j] = min(new_distance[j], abs(chicken[i][0] - house[j][0]) + abs(chicken[i][1] - house[j][1]))
        result = min(result, sum(new_distance))
        chicken_street(cnt + 1, new_distance, i + 1)


chicken_street(0, [100] * len(house), 0)
print(result)