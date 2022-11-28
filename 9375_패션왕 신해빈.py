from collections import defaultdict
import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n = int(input())
    clothes = defaultdict(lambda:1)
    for _ in range(n):
        clothes[input().split()[1]] += 1

    result = 1
    for key in clothes:
        result *= clothes[key]
    print(result - 1)