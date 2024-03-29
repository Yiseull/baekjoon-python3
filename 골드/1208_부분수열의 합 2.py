from collections import Counter


def calc_subset(set) -> Counter:
    subset = [0]
    for i in set:
        tmp = [i + j for j in subset]
        subset += tmp

    return Counter(subset)


def solve() -> int:
    x = calc_subset(seq[:n // 2])
    y = calc_subset(seq[n // 2:])

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
