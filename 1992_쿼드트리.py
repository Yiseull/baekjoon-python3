import sys
input = sys.stdin.readline

n = int(input())
screen = [input().strip() for _ in range(n)]


def dfs(x, y, length):
    if length == 1:
        return screen[x][y]

    half = length // 2
    a = dfs(x, y, half)
    b = dfs(x, y + half, half)
    c = dfs(x + half, y, half)
    d = dfs(x + half, y + half, half)

    if len(a) == 1 and a == b == c == d:    # len(a) == 1 <- 조건이 없으면 밑의 예제에서 틀림
        return a
    return '(' + a + b + c + d + ')'


print(dfs(0, 0, n))

'''
추가 예제
<입력>
8
00110011
00110011
11001100
11001100
00110011
00110011
11001100
11001100
<출력>
(0110)(0110)(0110)(0110)
'''