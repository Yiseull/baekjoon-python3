import sys
input = sys.stdin.readline


def solution() -> None:
    n, m = map(int, input().split() )
    balance = [int(input()) for _ in range(n)]
    left, right = max(balance), 1000000000

    while left < right:
        mid = (left + right) // 2
        cur, cnt = mid, 1

        for bal in balance:
            if cur < bal:
                cnt += 1
                cur = mid
            cur -= bal

        if cnt > m:
            left = mid + 1
        else:
            right = mid

    print(left)


solution()