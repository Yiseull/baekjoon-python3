import sys
from collections import Counter
input = sys.stdin.readline

while 1:
    s = input().rstrip()
    if s == '.':
        break

    if s.count('(') != s.count(')') or s.count('[') != s.count(']'):
        print('no')
        continue

    stack = ''
    for i in s:
        if i in '()[]':
            stack += i

    while '()' in stack or '[]' in stack:
        if '()' in stack:
            stack = stack.replace('()', '')
        if '[]' in stack:
            stack = stack.replace('[]', '')

    print('no' if stack else 'yes')