import sys
from bisect import bisect_left
input = sys.stdin.readline


p = int(input())
for t in range(1, p + 1):
    answer = 0
    arr = list(map(int, input().split()))[1:]
    sorted_arr = [0] * 20
    sorted_arr[0] = arr[0]
    for i in range(1, 20):
        if sorted_arr[i - 1] > arr[i]:
            index = bisect_left(sorted_arr[:i], arr[i])
            sorted_arr.insert(index, arr[i])
            answer += i - index
        else:
            sorted_arr[i] = arr[i]
    print(t, answer)