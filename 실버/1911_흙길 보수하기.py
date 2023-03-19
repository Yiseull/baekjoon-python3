import sys
input = sys.stdin.readline

n, l = map(int, input().split())
holes = [list(map(int, input().split())) for _ in range(n)]
holes.sort()
result, distance = 0, 0
for start, end in holes:
    if distance < start:
        distance = start
    cnt = (end - distance) // l
    if (end - distance) % l != 0:
        cnt += 1
    result += cnt
    distance += cnt * l
print(result)