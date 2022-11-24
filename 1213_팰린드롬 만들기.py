import collections

name = collections.Counter(sorted((input())))

palindrome = ''
center = ''
change = True
for key in name:
    if name[key] % 2 != 0:
        if len(center) == 0:
            center = key
        else:
            change = False
            break
    palindrome += key * (name[key] // 2)

if change:
    print(palindrome + center + palindrome[::-1])
else:
    print("I'm Sorry Hansoo")