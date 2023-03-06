import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = [*map(len, input().strip().replace('RR', '').split('R'))]
    n = int(input())
    x = input().strip()
    if sum(p) > n:
        print('error')
        continue
    if n:
        x = list(map(int, x[1:-1].split(',')))
    else:
        print('[]')
        continue

    error = 1
    start, end = 0, n
    for i, f in enumerate(p):
        if i % 2 == 0:
            start += f
        else:
            end -= f

    if error == -1:
        print('error')
    else:
        ans = '['
        if len(p) % 2 == 0:
            ans += ','.join(map(str, [x[i] for i in range(end - 1, start - 1, -1)]))
        else:
            ans += ','.join(map(str, [x[i] for i in range(start, end)]))
        print(ans + ']')