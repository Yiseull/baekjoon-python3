# N 입력
n = int(input())

# DP 테이블 0으로 초기화
dp = [0] * (n + 1)
dp[3] = 1
if n >= 5:
  dp[5] = 1
  for i in range(6, n + 1):
    # i-5킬로그램을 만들 수 있을 경우
    if dp[i - 5] != 0:
      dp[i] = dp[i - 5] + 1
    # i-3킬로그램을 만들 수 있을 경우
    elif dp[i - 3] != 0:
      dp[i] = dp[i - 3] + 1

if dp[n] == 0:
  print(-1)
else:
  print(dp[n])