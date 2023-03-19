import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemon1 = [None] * (n + 1)
pokemon2 = collections.defaultdict()
idx = 1
for i in range(n):
    name = input().strip()
    pokemon1[idx] = name
    pokemon2[name] = idx
    idx += 1

result = ''
problems = [input().strip() for _ in range(m)]
for problem in problems:
    if problem.isdigit():
        result += pokemon1[int(problem)] + '\n'
    else:
        result += str(pokemon2[problem]) + '\n'

print(result)