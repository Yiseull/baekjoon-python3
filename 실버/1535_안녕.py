import sys
input = sys.stdin.readline

n = int(input())
health = list(map(int, input().split()))
pleasure = list(map(int, input().split()))
result = 0


def backtracking(health_sum, pleasure_sum, i):
    if health_sum > 99:
        return

    if i == n:
        global result
        result = max(result, pleasure_sum)
        return

    backtracking(health_sum + health[i], pleasure_sum + pleasure[i], i + 1)
    backtracking(health_sum, pleasure_sum, i + 1)


backtracking(0, 0, 0)
print(result)