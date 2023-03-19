import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int, input().split()))
nums.sort()

count, left, right = 0, 0, n - 1
while left < right:
    sum = nums[left] + nums[right]
    if sum == m:
        count += 1
        left += 1
        right -= 1
    if sum < m:
        left += 1
    else:
        right -= 1

print(count)