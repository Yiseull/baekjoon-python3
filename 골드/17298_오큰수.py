import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
NGE = [-1] * n
stack = [0]
for i in range(n - 1):
    if A[i] < A[i + 1]:
        NGE[i] = A[i + 1]
        while stack and A[stack[-1]] < A[i + 1]:
            NGE[stack.pop()] = A[i + 1]
    else:
        stack.append(i)

print(' '.join(map(str, NGE)))