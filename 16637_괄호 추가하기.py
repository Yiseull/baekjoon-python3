import sys
input = sys.stdin.readline


def add_bracket(i, total):
    if i >= n:
        global answer
        answer = max(answer, total)
        return

    if data[i] == '+':
        if i + 4 <= n:
            add_bracket(i + 4, total + eval(data[i + 1:i + 4]))
        add_bracket(i + 2, total + int(data[i + 1]))
    elif data[i] == '-':
        if i + 4 <= n:
            add_bracket(i + 4, total - eval(data[i + 1:i + 4]))
        add_bracket(i + 2, total - int(data[i + 1]))
    elif data[i] == '*':
        if i + 4 <= n:
            add_bracket(i + 4, total * eval(data[i + 1:i + 4]))
        add_bracket(i + 2, total * int(data[i + 1]))


n = int(input())
data = input().strip()
answer = -2147483648
add_bracket(1, int(data[0]))
add_bracket(3, eval(data[0:3]))
print(answer)