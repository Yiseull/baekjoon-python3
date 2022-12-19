import sys
input = sys.stdin.readline


def printSeq(seq):
    if len(seq) == m:
        result = ''
        for i in seq:
            result += i + ' '
        print(result)
        return

    for i in range(1, n + 1):
        if str(i) not in seq:
            printSeq(seq + str(i))


n, m = map(int, input().split())
printSeq('')