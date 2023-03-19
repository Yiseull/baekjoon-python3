import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())
location = [int(input().strip()) for _ in range(j)]

left, right, result = 1, m, 0
for loc in location:
    if right < loc:
        distance = loc - right
        result += distance
        left += distance
        right += distance
    elif left > loc:
        distance = left - loc
        result += distance
        left -= distance
        right -= distance

print(result)