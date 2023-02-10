import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ps = input().strip()

    stack = []
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            if not stack or stack[-1] != '(':
                stack.append(0)
                break
            else:
                stack.pop()

    print('NO' if stack else 'YES')