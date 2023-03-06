import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().strip()
    while 'PP' in p:
        p = p.replace('PP', '')
    n = int(input())
    x = input().strip()
    if n:
        x = deque(map(int, x[1:-1].split(',')))
    else:
        if 'D' in p:
            print('error')
            continue
        else:
            print('[]')
            continue

    result = 1
    start, end = 0, n - 1
    for i, f in enumerate(p):
        if f == 'R':
            start, end = end, start
        else:
            if start < end:
                start += 1
            elif start > end:
                start -= 1
            else:
                if 'D' in p[i + 1:]:
                    result = -1
                    break
                else:
                    result = 0
                    break

    if result == -1:
        print('error')
    elif result == 0:
        print('[]')
    else:
        if x:
            ans = '['
            if start <= end:
                ans += ','.join(map(str, [x[i] for i in range(start, end + 1)]))
            else:
                ans += ','.join(map(str, [x[i] for i in range(start, end - 1, -1)]))
            print(ans + ']')
        else:
            print(x)