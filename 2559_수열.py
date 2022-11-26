n, k = map(int, input().split())
temperature = list(map(int, input().split()))

temp_sum = 0
for i in range(k):
    temp_sum += temperature[i]

result = temp_sum
for i in range(k, n):
    temp_sum += temperature[i] - temperature[i - k]
    if temp_sum > result:
        result = temp_sum

print(result)