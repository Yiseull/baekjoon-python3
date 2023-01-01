import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
a.sort()
left, right, cnt = 0, n - 1, 0
while left < right:
    sum = a[left] + a[right]
    if sum < x:
        left += 1
    else:
        if sum == x:
            cnt += 1
        right -= 1

print(cnt)