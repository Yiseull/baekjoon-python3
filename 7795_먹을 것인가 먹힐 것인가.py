import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i, result = 0, 0
    for a in A:
        while i < m and B[i] < a:
            i += 1
        result += i

    print(result)