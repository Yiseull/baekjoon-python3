import sys
input = sys.stdin.readline


def main() -> None:
    for _ in range(int(input())):
        n, m = map(int, input().split())
        airplane = [input() for _ in range(m)]
        print(n - 1)


main()
