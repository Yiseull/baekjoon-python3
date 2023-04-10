'''
현재 주유소보다 리터당 가격이 더 작은 주유소가 나올 때까지 이동하는 거리의 기름만 넣는다.
'''

import sys
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    length = list(map(int, input().split()))
    price = list(map(int, input().split()))

    result = 0
    distance, pre_price = 0, 1000000000
    for i in range(n - 1):
        if pre_price > price[i]:
            result += distance * pre_price
            distance, pre_price = length[i], price[i]
        else:
            distance += length[i]
    result += distance * pre_price

    print(result)


main()