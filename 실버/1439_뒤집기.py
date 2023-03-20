import sys
input = sys.stdin.readline

s = list(input().rstrip())
print(sum(s[i] != s[i - 1] for i in range(len(s))) // 2)
