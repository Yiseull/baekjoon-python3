import sys
input = sys.stdin.readline


def make_password(cons, vow, s, index):
    if cons + vow == l and cons > 1 and vow > 0:
        global answer
        answer += s + '\n'
        return

    for i in range(index, c):
        if alpha[i] in 'aeiou':
            make_password(cons, vow + 1, s + alpha[i], i + 1)
        else:
            make_password(cons + 1, vow, s + alpha[i], i + 1)


l, c = map(int, input().split())
alpha = input().split()
alpha.sort()
answer = ''
make_password(0, 0, '', 0)
print(answer)