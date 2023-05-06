from bisect import bisect_left, bisect_right
from itertools import combinations


def count(subset, target) -> int:
    return bisect_right(subset, target) - bisect_left(subset, target)


def calc_subset(set, subset, n) -> None:
    for i in range(1, n + 1):
        for comb in combinations(set, i):
            subset.append(sum(comb))


def solve() -> int:
    x = []
    y = []

    calc_subset(seq[:n // 2], x, n // 2)
    calc_subset(seq[n // 2:], y, n - n // 2)

    x.sort()
    y.sort()

    cnt = 0
    for i in x:
        cnt += count(y, s - i)

    cnt += count(x, s)
    cnt += count(y, s)

    return cnt


if __name__ == '__main__':
    n, s = map(int, input().split())
    seq = list(map(int, input().split()))
    print(solve())
