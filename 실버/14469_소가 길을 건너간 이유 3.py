import sys
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort()
result = 0
for arrival, checkin in times:
    if result < arrival:
        result = arrival + checkin
    else:
        result += checkin

print(result)