import sys
from collections import Counter

input = sys.stdin.readline

n, c = map(int, input().split())
message = Counter(map(int, input().split()))

for x in message.most_common():
    for _ in range(x[1]):
        print(x[0], end=' ')