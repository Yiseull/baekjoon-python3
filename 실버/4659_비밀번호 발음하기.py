import sys
input = sys.stdin.readline

vowel = set(['a', 'e', 'i', 'o', 'u'])
while 1:
    password = input().strip()
    if password == 'end':
        break

    condition1, condition2_con, condition2_vow, condition3 = False, 0, 0, False
    for i, char in enumerate(password):
        if char in vowel:
            condition1 = True

        if char not in vowel:
            condition2_vow = 0
            condition2_con += 1
            if condition2_con == 3:
                break

        if char in vowel:
            condition2_con = 0
            condition2_vow += 1
            if condition2_vow == 3:
                break

        if i > 0 and password[i - 1] == char:
            if char == 'e' or char == 'o':
                continue
            condition3 = True
            break

    if not condition1 or condition2_con > 2 or condition2_vow > 2 or condition3:
        print('<' + password + '> is not acceptable.')
        continue

    print('<' + password + '> is acceptable.')