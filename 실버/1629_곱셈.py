import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

dp = [a]
power, i = 1, 0
while 1:
    power *= 2
    if power > b:
        break
    dp.append(dp[i] * dp[i] % c)
    i += 1

result = 1
while 1:
    multiple = pow(2, i)
    if b - multiple >= 0:
        result = result * dp[i] % c
        b -= multiple
        if b == 0:
             break
    i -= 1

print(result)