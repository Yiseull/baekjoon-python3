n = int(input())
pattern = input()
files = [input() for _ in range(n)]

idx = pattern.find('*')
left, right = pattern[:idx], pattern[idx + 1:]
for file in files:
    # 예외 처리
    if len(pattern) - 1 > len(file):
        print("NE")
        continue
    # 별표(*)의 왼쪽 문자열과 오른쪽 문자열이 일치하는지 확인
    if left != file[:idx] or right != file[len(file) - len(right):]:
        print("NE")
        continue
    print("DA")