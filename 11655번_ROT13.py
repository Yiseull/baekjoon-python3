s = input()

for i in range(len(s)):
    if s[i].isalpha():
        code = ord(s[i]) + 13
        if (s[i].islower() and code > 122) or (s[i].isupper() and code > 90):
            code -= 26
        print(chr(code), end='')
    else:
        print(s[i], end='')