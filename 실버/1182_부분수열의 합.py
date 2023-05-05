def dfs(idx, sum, cnt) -> None:
    if sum == s and cnt > 0:
        global answer
        answer += 1

    for i in range(idx, n):
        dfs(i + 1, sum + sequence[i], cnt + 1)


n, s = map(int, input().split())
sequence = tuple(map(int, input().split()))
answer = 0
dfs(0, 0, 0)
print(answer)
