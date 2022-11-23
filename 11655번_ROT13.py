s = input()

for i in s:
    if i.islower():
        code = ord(i) + 13
        if code > 122:
            code -= 26
        print(chr(code), end='')
    elif i.isupper():
        code = ord(i) + 13
        if code > 90:
            code -= 26
        print(chr(code), end='')
    else:
        print(i, end='')
