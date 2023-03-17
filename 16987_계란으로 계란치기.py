import sys
input = sys.stdin.readline


def count_broken():
    cnt = 0
    for egg in eggs:
        if egg[0] <= 0:
            cnt += 1
    return cnt


def dfs(index):
    if index == n:
        global answer
        answer = max(answer, count_broken())
        return

    # 손에 든 계란이 깨져있다면, 오른쪽 계란으로 넘어간다.
    if eggs[index][0] <= 0:
        dfs(index + 1)
    else:
        all_broken = True
        for i, egg in enumerate(eggs):
            # 손에 든 계란이거나 이미 깨진 계란은 치지 않고 넘어간다.
            if i == index or egg[0] <= 0:
                continue
            all_broken = False
            eggs[i][0] -= eggs[index][1]
            eggs[index][0] -= eggs[i][1]
            dfs(index + 1)
            eggs[i][0] += eggs[index][1]
            eggs[index][0] += eggs[i][1]

        # 모든 계란이 깨져있다면, dfs를 빠져나온다.
        if all_broken:
            dfs(n)


n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
answer = 0
if n == 1:
    print(0)
else:
    dfs(0)
    print(answer)