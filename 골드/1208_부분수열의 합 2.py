from collections import Counter
from itertools import combinations


def calc_subset(set, subset, n) -> None:
    for i in range(1, n + 1):
        for comb in combinations(set, i):
            subset.append(sum(comb))


def solve() -> int:
    x = [0]
    y = [0]

    calc_subset(seq[:n // 2], x, n // 2)
    calc_subset(seq[n // 2:], y, n - n // 2)

    x = Counter(x)
    y = Counter(y)

    answer = 0
    for i in x:
        target = s - i
        if target in y:
            answer += x[i] * y[target]

    return answer if s != 0 else answer - 1


if __name__ == '__main__':
    n, s = map(int, input().split())
    seq = list(map(int, input().split()))
    print(solve())
