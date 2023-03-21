exp = input().split('-')
answer = sum(map(int, exp[0].split('+')))
for i in range(1, len(exp)):
    answer -= sum(map(int, exp[i].split('+')))
print(answer)