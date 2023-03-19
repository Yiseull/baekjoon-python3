import sys
input = sys.stdin.readline

n = int(input())
contents = [input().strip() for _ in range(n)]

result = []
for i, content in enumerate(contents):
    s = ''
    for c in content:
        if c.isdigit():
            s += c
        elif len(s) > 0:
            result.append(int(s))
            s = ''
    if len(s) > 0:
        result.append(int(s))

for num in sorted(result):
    print(num)