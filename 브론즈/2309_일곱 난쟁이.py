height = []
diff = -100

# 입력
for i in range(9):
    a = int(input())
    height.append(a)
    diff += a

height.sort()

find = False
for i in range(8):
    for j in range(i + 1, 9):
        if height[i] + height[j] == diff:
            find = True
            for k, h in enumerate(height):
                if k == i or k == j:
                    continue
                print(h)
            break
    if find == True:
        break