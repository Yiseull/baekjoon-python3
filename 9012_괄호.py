import sys
ps = sys.stdin.readlines()[1:]

for i in ps:
    i = i.rstrip()
    while '()' in i:
        i = i.replace('()', '')

    if i:
        print('NO')
    else:
        print('YES')