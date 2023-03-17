import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline


def count_s(seven):
    cnt_s, cnt_y = 0, 0
    for x in seven:
        if sy[x // 5][x % 5] == 'S':
            cnt_s += 1
        else:
            cnt_y += 1
            if cnt_y > 3:
                return False
    return True


def bfs(seven):
    visited = [False] * 25
    visited[seven[0]] = True
    q = deque([seven[0]])
    cnt = 0
    while q:
        v = q.popleft()
        cnt += 1
        for w in [v - 5, v - 1, v + 1, v + 5]:
            # w가 맨 왼쪽 자리거나 맨 오른쪽 자리인 경우는 제외
            if (v % 5 == 4 and w == v + 1) or (v % 5 == 0 and w == v -1):
                continue
            if 0 <= w < 25 and w in seven and not visited[w]:
                visited[w] = True
                q.append(w)

    if cnt == 7:
        return True
    return False


sy = [list(input().rstrip()) for _ in range(5)]
answer = 0
# 조합을 이용해 7명 뽑기
for combi in combinations([i for i in range(25)], 7):
    # 7명 중 '이다솜파' 학생이 적어도 4명 이상인지 확인
    if not count_s(combi):
        continue
    # 7명의 자리가 서로 인접한지 확인
    if bfs(combi):
        answer += 1
print(answer)
