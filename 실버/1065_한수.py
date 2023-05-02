def han_num(x) -> bool:
    x = tuple(map(int, str(x)))
    a = x[1] - x[0]
    for i in range(2, len(x)):
        if x[i] - x[i - 1] != a:
            return False

    return True


def main() -> None:
    n = int(input())
    answer = 0
    for i in range(1, n + 1):
        if i < 10:
            answer += 1
            continue

        if han_num(i):
            answer += 1

    print(answer)


main()