# 알고리즘 분류:

import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

stack = []
cnt = 0
for word in words:
    stack.clear()
    for c in word:
        if len(stack) != 0 and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    if len(stack) == 0:
        cnt += 1

print(cnt)