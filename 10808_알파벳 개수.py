import collections

count = collections.Counter(input())

for i in range(97, 123):
    if chr(i) in count:
        print(count[chr(i)], end=' ')
    else:
        print(0, end=' ')