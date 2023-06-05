import sys
from itertools import combinations
input = sys.stdin.readline


def check(words, learn) -> int:
    tmp = 0
    for word in words:
        possible = True
        for w in word:
            if learn[ord(w)] == 0:
                possible = False
                break
        if possible:
            tmp += 1
    return tmp


def solution() -> None:
    n, k = map(int, input().split())
    words = [input().rstrip()[4:-4] for _ in range(n)]
    remain_alpha = set(chr(i) for i in range(97, 123)) - {'a', 'n', 't', 'i', 'c'}

    answer = 0
    if k > 4:
        learn = [0] * 123
        for w in ('a', 'n', 't', 'i', 'c'):
            learn[ord(w)] = 1

        for com in combinations(remain_alpha, k - 5):
            for c in com:
                learn[ord(c)] = 1

            answer = max(answer, check(words, learn))

            for c in com:
                learn[ord(c)] = 0

    print(answer)


solution()