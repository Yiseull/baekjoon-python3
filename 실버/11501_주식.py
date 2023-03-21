import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    days = list(map(int, input().split()))
    profit = 0
    max = 0
    for i in range(n - 1, -1, -1):
        if days[i] > max:
            max = days[i]
        elif days[i] < max:
            profit += max - days[i]

    print(profit)