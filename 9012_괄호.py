import sys
input = sys.stdin.readline

for _ in range(int(input())):
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

    if stack:
        print('NO')
    else:
        print('YES')