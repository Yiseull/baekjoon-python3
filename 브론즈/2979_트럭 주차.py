fee = list(map(int, input().split()))
times = []
for _ in range(3):
    t1, t2 = map(int, input().split())
    times.append([t1, 0])
    times.append([t2, 1])

times.sort()

result, car, pre = 0, 0, 0
for time in times:
    result += car * fee[car - 1] * (time[0] - pre)
    if time[1] == 0:
        car += 1
    else:
        car -= 1
    pre = time[0]

print(result)
