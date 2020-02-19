import collections

n = int(input())
S = [input() for i in range(n)]
c = collections.Counter(S)
m = c.most_common()[0][1]

for j in c:
    if m == int(c.most_common()[0][1]):
        print(c.most_common()[0][0])
        c.pop(0)