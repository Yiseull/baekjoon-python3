import sys
input = sys.stdin.readline


def solution() -> None:
    n, m = map(int, input().split())
    unheard = set(input().rstrip() for _ in range(n))
    unseen = set(input().rstrip() for _ in range(m))
    unheard_unseen = unheard & unseen

    print(len(unheard_unseen))
    print('\n'.join(sorted(unheard_unseen)))


solution()
