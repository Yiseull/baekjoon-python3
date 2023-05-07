def main() -> None:
    n = int(input())
    arr = tuple(map(int, input().split()))
    stack = [(arr[-1], n - 1)]
    answer = [0] * n
    for i in range(n - 2, -1, -1):
        while stack and arr[i] >= stack[-1][0]:
            answer[stack.pop()[1]] = i + 1

        stack.append((arr[i], i))

    print(' '.join(map(str, answer)))


main()
