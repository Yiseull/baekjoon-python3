import sys

n = int(sys.stdin.readline())

if n < 0:
    print(32)   # 음수인 경우 부호를 나타내기 위해 항상 32비트가 필요!
else:
    print(len(bin(n)) - 2)