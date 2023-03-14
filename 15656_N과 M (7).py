import sys
input = sys.stdin.readline


def print_per(index, s, cnt):
    if cnt == m:
        print(s)
        return

    for i in range(n):
        print_per(i, s + str(nums[i]) + ' ', cnt + 1)


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
print_per(0, '', 0)