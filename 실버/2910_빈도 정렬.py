import sys
from collections import Counter

input = sys.stdin.readline

n, c = map(int, input().split())
message = Counter(map(int, input().split()))

result = ''
for x in message.most_common():
    for _ in range(x[1]):
        result += str(x[0]) + ' '

print(result)