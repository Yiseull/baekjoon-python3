import sys
input = sys.stdin.readline

for line in sys.stdin:
    n = int(line)
    num = 1
    length = 1
    while True:
        if num % n == 0:
            print(length)
            break
        num = num * 10 + 1
        length += 1