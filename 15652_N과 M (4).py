import sys
input = sys.stdin.readline


def print_per(num, s):
    if len(s) == m * 2:
        print(s)
        return

    for i in range(num, n + 1):
        if i == 0:
            continue
        print_per(i, s + str(i) + ' ')


n, m = map(int, input().split())
print_per(0, '')