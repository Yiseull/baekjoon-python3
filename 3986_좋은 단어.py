import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

cnt = 0
for word in words:
    stack = []
    for c in word:
        if len(stack) != 0 and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    if len(stack) == 0:
        cnt += 1

print(cnt)