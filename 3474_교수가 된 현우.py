import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    result, i = 0, 5
    while i <= n:
        result += n // i
        i *= 5

    print(result)