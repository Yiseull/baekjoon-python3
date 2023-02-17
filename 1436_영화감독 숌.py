import sys
input = sys.stdin.readline

n = int(input())
end = '666'
result = ''
i, cnt = 0, 0
while cnt < n:
    if str(i)[-1] == '6':
        ten = 2
        while len(str(i)) >= ten and str(i)[-ten] == '6':
            ten += 1
        ten -= 1
        tmp = str(i)
        if ten < 3:
            tmp += '6' * (3 - ten)
        for j in range(pow(10, ten)):
            result = tmp + str(j).zfill(ten)
            cnt += 1
            if cnt == n:
                break
    else:
        result = str(i) + end
        cnt += 1
    i += 1

print(int(result))