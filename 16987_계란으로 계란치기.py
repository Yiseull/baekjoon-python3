import sys
input = sys.stdin.readline


def dfs(index, broken_cnt):
    if index == n:
        global answer
        answer = max(answer, broken_cnt)
        return

    # 손에 든 계란이 깨졌다면 다음 계란으로 넘어 간다.
    if eggs[index][0] <= 0:
        dfs(index + 1, broken_cnt)
    else:
        all_broken = True
        for i, egg in enumerate(eggs):
            # 손에 든 계란 or 이미 깨진 계란 이라면 치지 않고 넘어 간다.
            if i == index or egg[0] <= 0:
                continue
            all_broken = False
            eggs[i][0] -= eggs[index][1]
            eggs[index][0] -= eggs[i][1]
            tmp = broken_cnt
            if eggs[i][0] <= 0:
                tmp += 1
            if eggs[index][0] <= 0:
                tmp += 1
            dfs(index + 1, tmp)
            eggs[i][0] += eggs[index][1]
            eggs[index][0] += eggs[i][1]

        # 손에 든 계란을 제외한 모든 계란이 깨져 있는 경우
        if all_broken:
            answer = max(answer, n - 1)


n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
answer = 0
if n == 1:
    print(0)
else:
    dfs(0, 0)
    print(answer)