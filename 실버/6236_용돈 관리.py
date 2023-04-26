import sys
input = sys.stdin.readline


def solution() -> None:
    n, m = map(int, input().split())
    balance = [int(input()) for _ in range(n)]
    result = 1000000000
    left, right = min(balance), 1000000000

    while left <= right:
        mid = (left + right) // 2
        cur, cnt = 0, 0

        for bal in balance:
            if cur < bal:
                cnt += 1
                cur = mid
            cur -= bal
            if cur < 0 or cnt > m:
                cnt = m + 1
                break

        if cnt > m:
            left = mid + 1
        else:
            result = min(result, mid)
            right = mid - 1

    print(result)


solution()