import sys
input = sys.stdin.readline

s = input().rstrip()
explosion = input().rstrip()
explosion_len = len(explosion)

stack = []
for char in s:
    stack.append(char)
    if char == explosion[-1] and ''.join(stack[-explosion_len:]) == explosion:
        for _ in range(explosion_len):
            stack.pop()

print('FRULA' if len(stack) == 0 else ''.join(stack))