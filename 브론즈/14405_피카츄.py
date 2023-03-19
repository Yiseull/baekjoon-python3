import sys

s = sys.stdin.readline().rstrip()
s = s.replace('pi', ' ')    # ''으로 치환했을 때 실패. 반례: kpia
s = s.replace('ka', ' ')
s = s.replace('chu', ' ')

print('YES' if s.strip() == '' else 'NO')