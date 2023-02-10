import sys
input = sys.stdin.readline

# 입력
n = int(input())
info = [[] for _ in range(n)]
for i in range(n):
    team, time = input().split()
    minute, second = map(int, time.split(':'))
    info[i] = [team, minute, second]

# 득점 시간 순으로 오름차순 정렬
info.sort(key=lambda x: (x[1], x[2]))
score1, score2 = 0, 0
time1, time2, before = [0, 0], [0, 0], [0, 0]
for team, minute, second in info:
    # 직전의 득점한 시간부터 현재 득점한 시간까지 이기고 있는 팀의 시간 계산
    if score1 < score2:
        if second >= before[1]:
            time2[0] += minute - before[0]
            time2[1] += second - before[1]
        else:
            time2[0] += minute - before[0] - 1
            time2[1] += second - before[1] + 60
    elif score1 > score2:
        if second >= before[1]:
            time1[0] += minute - before[0]
            time1[1] += second - before[1]
        else:
            time1[0] += minute - before[0] - 1
            time1[1] += second - before[1] + 60

    # 득점한 팀의 스코어 1 더하기
    if team == '1':
        score1 += 1
    else:
        score2 += 1
    before = [minute, second]

# 경기 끝날 때 이기고 있던 팀 시간 계산
if score1 < score2:
    time2[0] += 47 - before[0]
    time2[1] += 60 - before[1]
elif score1 > score2:
    time1[0] += 47 - before[0]
    time1[1] += 60 - before[1]

# 누적된 초가 60초가 넘었을 경우
if time1[1] > 59:
    time1[0] += time1[1] // 60
    time1[1] %= 60
if time2[1] > 59:
    time2[0] += time2[1] // 60
    time2[1] %= 60

# 출력
print(str(time1[0]).zfill(2) + ':' + str(time1[1]).zfill(2))
print(str(time2[0]).zfill(2) + ':' + str(time2[1]).zfill(2))