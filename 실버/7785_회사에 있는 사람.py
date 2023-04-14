import sys
input = sys.stdin.readline


def main() -> None:
    enter = set()

    for _ in range(int(input())):
        name, record = input().split()
        if record == 'enter':
            enter.add(name)
        elif name in enter:
            enter.remove(name)

    print('\n'.join(sorted(enter, reverse=True)))


main()
