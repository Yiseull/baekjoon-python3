import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    rankings = [0] * (n + 1)
    for _ in range(n):
        a, b = map(int, input().split())
        rankings[a] = b

    answer = 1
    min_rank = rankings[1]
    for i in range(2, n + 1):
        if min_rank < rankings[i]:
            continue
        min_rank = min(min_rank, rankings[i])
        answer += 1

    print(answer)
