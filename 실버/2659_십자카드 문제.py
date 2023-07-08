import sys
input = sys.stdin.readline


def find_clock_num(num) -> str:
    return min(num, num[1:] + num[0], num[2:] + num[:2], num[3] + num[:3])


def count(num, clock_num) -> None:
    if len(num) == 4:
        if num == find_clock_num(num):
            global cnt
            cnt += 1
            if num == clock_num:
                print(cnt)
                exit(0)
        return

    for i in range(1, 10):
        count(num + str(i), clock_num)


def solution() -> None:
    cards = ''.join(input().split())
    clock_num = find_clock_num(cards)
    count('', clock_num)


cnt = 0
solution()
print(cnt)
