# 정수 N 입력
n = int(input())

# DP 테이블 초기화
dp = [0] * (n + 1)

# 다이나믹 프로그래밍 - 보텀업
for i in range(2, n + 1):
    # 1 빼기 연산 수행
    dp[i] = dp[i - 1] + 1
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])