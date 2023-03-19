import collections

n = int(input())
first_name = collections.defaultdict(int)
for _ in range(n):
    name = input()
    first_name[name[0]] += 1

select = ''
for key in first_name:
    if first_name[key] > 4:
        select += key

if len(select) > 0:
    print(''.join(sorted(select)))
else:
    print("PREDAJA")