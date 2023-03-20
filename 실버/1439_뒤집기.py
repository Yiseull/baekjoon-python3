import sys
input = sys.stdin.readline

S = list(input().rstrip())
current, cnt = S[0], 1
for s in S:
    if current != s:
        cnt += 1
        current = s
print(cnt // 2 if cnt > 0 else 0)