import sys
input = sys.stdin.readline


def count_horizontal_space(room) -> int:  # 가로로 누울 수 있는 자리
    cnt = 0
    for row in room:
        for space in row.split('X'):
            if len(space) > 1:
                cnt += 1

    return cnt


def count_vertical_space(room, n) -> int:  # 세로로 누울 수 있는 자리
    cnt = 0
    for j in range(n):
        tmp = 0
        for i in range(n):
            if room[i][j] == '.':
                tmp += 1
            else:
                if tmp > 1:
                    cnt += 1
                tmp = 0
        if tmp > 1:
            cnt += 1
    return cnt


def solution():
    n = int(input())
    room = tuple((input().rstrip()) for _ in range(n))
    return count_horizontal_space(room), count_vertical_space(room, n)


cnt_row, cnt_col = solution()
print(cnt_row, cnt_col)
