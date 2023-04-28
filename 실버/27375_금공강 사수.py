'''
고려 사항
1. 금공강
2. 총 k 학점
3. 수업끼리 겹치면 안됨
'''

import sys
input = sys.stdin.readline


def solution(idx, total, before) -> None:
    if total > k:
        return

    if total == k:
        global answer
        answer += 1
        return

    for i in range(idx, n):
        if lectures[i][0] == 5:
            continue
        if before != -1 and lectures[before][0] == lectures[i][0] and lectures[before][2] >= lectures[i][1]:
            continue
        solution(i + 1, total + lectures[i][2] - lectures[i][1] + 1, i)


if __name__ == '__main__':
    n, k = map(int, input().split())
    lectures = [tuple(map(int, input().split())) for _ in range(n)]
    lectures.sort(key=lambda x: (x[0], x[1], x[2]))
    answer = 0
    solution(0, 0, -1)
    print(answer)
