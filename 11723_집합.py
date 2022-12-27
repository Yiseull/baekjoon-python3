import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    oper = list(input().split())
    if oper[0] == 'add':
        s.add(oper[1])
    elif oper[0] == 'remove':
        x = oper[1]
        if x in s:
            s.remove(x)
    elif oper[0] == 'check':
        print(1 if oper[1] in s else 0)
    elif oper[0] == 'toggle':
        x = oper[1]
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif oper[0] == 'all':
        s = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'}
    elif oper[0] == 'empty':
        s.clear()