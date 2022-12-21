import sys
input = sys.stdin.readline

k = int(input())
nums = list(map(int, input().split()))
level = [[] for _ in range(k)]


def inorder(i, start, end):
    if start == end:
        level[i].append(nums[start])
        return

    mid = (start + end) // 2
    inorder(i + 1, start, mid - 1)
    level[i].append(nums[mid])
    inorder(i + 1, mid + 1, end)


inorder(0, 0, len(nums) - 1)
result = ''
for i in range(k):
    for l in level[i]:
        result += str(l) + ' '
    result += '\n'
print(result)