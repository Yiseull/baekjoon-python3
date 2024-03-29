import sys
input = sys.stdin.readline


def find(parent, x) -> int:
    if parent[x] == x:
        return x
    return find(parent, parent[x])


def union(parent, a, b) -> None:
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    parent = [i for i in range(n + 1)]
    result, cnt = 0, 0

    edges.sort(key=lambda x: x[2])

    for a, b, c in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += c
            cnt += 1
            if cnt == n - 2:
                break

    print(result)
