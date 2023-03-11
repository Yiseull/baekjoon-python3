import sys
input = sys.stdin.readline


def print_per(number, s):
    if len(s) == m * 2:
        print(s)
        return

    for i in range(number, n + 1):
        print_per(i, s + str(i) + ' ')


n, m = map(int, input().split())
print_per(1, '')