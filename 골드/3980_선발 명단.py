import sys
input = sys.stdin.readline


def solution(idx, total) -> None:
    if idx == 11:
        global result
        result = max(result, total)
        return

    for i, s in enumerate(stats[idx]):
        if s and not visited[i]:
            visited[i] = True
            solution(idx + 1, total + s)
            visited[i] = False


if __name__ == '__main__':
    for _ in range(int(input())):
        stats = [list(map(int, input().split())) for _ in range(11)]
        visited = [False] * 11
        result = 0
        solution(0, 0)
        print(result)
