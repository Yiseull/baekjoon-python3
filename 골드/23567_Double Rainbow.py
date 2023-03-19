import sys
from collections import Counter, defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
points = [int(input().strip()) for _ in range(n)]
counter = Counter(points)
double_rainbow = defaultdict(int)

for i in range(k):
    double_rainbow[points[i]] += 1
    counter[points[i]] -= 1

result, left, right = n, 0, k
while left < n and right < n:
    if len(double_rainbow) == k and 0 not in double_rainbow.values():
        if 0 not in counter.values():
            result = min(result, sum(double_rainbow.values()))
        double_rainbow[points[left]] -= 1
        counter[points[left]] += 1
        left += 1
    else:
        double_rainbow[points[right]] += 1
        counter[points[right]] -= 1
        right += 1

print(0 if result == n else result)