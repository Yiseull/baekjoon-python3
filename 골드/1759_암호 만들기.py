import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()
answer = ''
for per in combinations(alpha, l):
    vow = 0
    for p in per:
        if p in 'aeiou':
            vow += 1

    if vow > 0 and l - vow > 1:
        answer += ''.join(per) + '\n'
print(answer)