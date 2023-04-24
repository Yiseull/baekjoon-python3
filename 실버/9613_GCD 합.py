import sys
from itertools import combinations
input = sys.stdin.readline


def gcd(a, b) -> int:
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    for _ in range(int(input())):
        arr = tuple(map(int, input().split()))
        result = 0
        for a, b in combinations(arr[1:], 2):
            result += gcd(a, b)
        print(result)
