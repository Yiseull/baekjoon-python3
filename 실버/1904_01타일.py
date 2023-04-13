def main() -> None:
    n = int(input())
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(n - 2):
        a, b = b, (a + b) % 15746

    return b


print(main())
