import sys
input = sys.stdin.readline


def main() -> None:
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    move = [list(map(int, input().split())) for _ in range(m)]
    cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

    for d, s in move:
        visited = set()
        i, j = 0, 0
        # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
        if 5 < d < 9: i = 1 * s
        elif 1 < d < 5: i = -1 * s
        if 3 < d < 7: j = 1 * s
        elif 0 < d < 3 or d == 8: j = -1 * s

        for c in cloud:
            # 1. 모든 구름이 d 방향으로 s칸 이동
            c[0] += i
            c[1] += j
            while c[0] < 0: c[0] += n
            while c[0] >= n: c[0] -= n
            while c[1] < 0: c[1] += n
            while c[1] >= n: c[1] -= n

            # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가
            a[c[0]][c[1]] += 1

        # 4. 물복사버그 마법 시전
        for c in cloud:
            cnt = 0
            for dx, dy in [[-1, -1], [-1, 1], [1, 1], [1, -1]]:
                next_x = dx + c[0]
                next_y = dy + c[1]
                if 0 <= next_x < n and 0 <= next_y < n and a[next_x][next_y]:
                    cnt += 1
            a[c[0]][c[1]] += cnt
            visited.add((c[0], c[1]))

        # 5. 구름 생성
        new_cloud = []
        for x in range(n):
            for y in range(n):
                if a[x][y] > 1 and (x, y) not in visited:
                    a[x][y] -= 2
                    new_cloud.append([x, y])
        cloud = new_cloud

    return sum(map(sum, a))


print(main())
