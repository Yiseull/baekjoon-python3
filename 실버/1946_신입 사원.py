import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    rankings = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
    answer = 0
    min_rank = 0
    for i, ranking in enumerate(rankings):
        if i == 0:
            answer += 1
            min_rank = ranking[1]
            continue

        if min_rank < ranking[1]:
            continue

        min_rank = min(min_rank, ranking[1])
        answer += 1

    print(answer)
