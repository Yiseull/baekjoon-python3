import sys
input = sys.stdin.readline

while 1:
    s = input().rstrip()
    if s == '.':
        break

    stack = []
    for i in s:
        if i in '([':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                stack.append(0)
                break
            stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[':
                stack.append(0)
                break
            stack.pop()

    print('no' if stack else 'yes')