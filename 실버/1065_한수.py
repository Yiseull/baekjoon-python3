def han_num(x) -> bool:
    x = tuple(map(int, str(x)))
    a = x[1] - x[0]
    for i in range(2, len(x)):
        if x[i] - x[i - 1] != a:
            return False

    return True


def main() -> int:
    n = int(input())
    if n < 100:
        return n

    answer = 99
    for i in range(100, n + 1):
        if i < 10:
            answer += 1
            continue

        if han_num(i):
            answer += 1

    return answer


print(main())