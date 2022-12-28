import sys
from collections import Counter

x = int(sys.stdin.readline())
counter = Counter(bin(x))
print(counter['1'])