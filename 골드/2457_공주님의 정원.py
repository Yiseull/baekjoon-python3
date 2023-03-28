import sys
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    flowers = [list(map(int, input().split())) for _ in range(n)]
    flowers.sort(key=lambda x: (x[0], x[1]))
    start, end, cnt = [3, 1], [3, 1], 0
    count = False
    for flower in flowers:
        if flower[0] < start[0] or (flower[0] == start[0] and flower[1] <= start[1]):
            if flower[2] > end[0] or (flower[2] == end[0] and flower[3] > end[1]):
                end = [flower[2], flower[3]]
        elif flower[0] < end[0] or (flower[0] == end[0] and flower[1] <= end[1]):
            cnt += 1
            if end[0] == 12:
                count = True
                break
            start = end[:]
            end = [flower[2], flower[3]]
    if end[0] == 12:
        print(cnt if count else cnt + 1)
    else:
        print(0)


main()