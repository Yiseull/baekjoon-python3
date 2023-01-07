import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))
result, left, right = 10000, 1, sum(lectures)
while left <= right:
    mid, cnt, size = (left + right) // 2, 1, 0
    for lecture in lectures:
        if lecture > mid:
            cnt = m + 1
            break
        size += lecture
        if size > mid:
            size = lecture
            cnt += 1
    if cnt <= m:
        right = mid - 1
        result = mid
    else:
        left = mid + 1

print(result)