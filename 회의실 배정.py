n = int(input())

time = []
for _ in range(n):
    a, b = map(int, input().split())
    # 끝나는 시간, 시작 시간 순으로
    time.append([b,a])

# 끝나는 시간을 기준으로 오름차순 정렬
time.sort()

# 사용할 수 있는 회의 수 count, 직전 회의 끝나는 시간 end
count, end = 0, 0
for i in time:
    # 직전 회의랑 겹치지 않으면 선택
    if end <= i[1]:
        count += 1
        end = i[0]

print(count)