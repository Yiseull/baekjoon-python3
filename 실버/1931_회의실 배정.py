import sys
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key=lambda x: (x[1], x[0]))
print(times)
cnt, present = 0, 0
for start, end in times:
    if present <= start:
        present = end
        cnt += 1
print(cnt)