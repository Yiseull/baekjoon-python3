import sys
input = sys.stdin.readline

k = int(input())
A = list(input().split())
result = []


def is_satisfied(pre, i, num, remain):
    if i == k:
        global result
        result.append(int(num))
        return

    new_remain = remain.copy()
    if A[i] == '>':
        for n in remain:
            if pre > n:
                new_remain.remove(n)
                is_satisfied(n, i + 1, num + str(n), new_remain)
                new_remain.add(n)
    else:
        for n in remain:
            if pre < n:
                new_remain.remove(n)
                is_satisfied(n, i + 1, num + str(n), new_remain)
                new_remain.add(n)


nums = set([i for i in range(10)])
for i in range(10):
    nums.remove(i)
    is_satisfied(i, 0, str(i), nums)
    nums.add(i)
result.sort()
print(str(result[-1]).zfill((k + 1)))
print(str(result[0]).zfill((k + 1)))