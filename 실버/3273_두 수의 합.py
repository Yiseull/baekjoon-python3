import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
a.sort()
a_set = set(a)
cnt = 0
for i in a:
    if x - i in a_set:
        cnt += 1

print(cnt // 2)