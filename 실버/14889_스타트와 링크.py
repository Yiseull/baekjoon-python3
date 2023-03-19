import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]
combination = list(combinations([i for i in range(n)], n // 2))


def team_stats(index):
    power = 0
    for i, j in combinations(combination[index], 2):
        power += stats[i][j] + stats[j][i]
    return power


result = 100
for i in range(len(combination) // 2):
    result = min(result, abs(team_stats(i) - team_stats(-(i + 1))))
print(result)