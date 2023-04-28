'''
고려 사항
1. 금공강
2. 총 k 학점
3. 수업끼리 겹치면 안됨
'''

import sys
input = sys.stdin.readline


def check(s, e, schedule) -> bool:
    for si, ei in schedule:
        if si <= s <= ei or si <= e <= ei or s <= si <= e or s <= ei <= e:
            return False
    return True


def solution(idx, total) -> None:
    if total > k:
        return

    if total == k:
        global answer
        answer += 1
        return

    for i in range(idx, n):
        w, s, e = lectures[i]
        if w == 5:
            continue

        if check(s, e, schedule[w - 1]):
            new_schedule = schedule[w - 1][:]
            schedule[w - 1].append((s, e))
            solution(i + 1, total + e - s + 1)
            schedule[w - 1] = new_schedule


n, k = map(int, input().split())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
schedule = [[] for _ in range(4)]
answer = 0
solution(0, 0)
print(answer)
