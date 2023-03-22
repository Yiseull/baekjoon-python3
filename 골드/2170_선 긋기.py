import sys
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    lines.sort(key=lambda x: x[0])
    length, start, end = 0, lines[0][0], lines[0][1]  # start, end 초기화 주의 (-1,000,000,000 ≤ x < y ≤ 1,000,000,000)
    for x, y in lines:
        if x > end:
            length += end - start
            start, end = x, y
        elif end < y:
            end = y
    length += end - start
    print(length)


main()