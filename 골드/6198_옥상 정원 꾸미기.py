import sys
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    building = [int(input()) for _ in range(n)]
    building.append(1000000000)
    answer = 0
    stack = []
    for i, h in enumerate(building):
        while stack and stack[-1][0] <= h:
            answer += i - stack.pop()[1] - 1

        stack.append((h, i))

    print(answer)


main()
