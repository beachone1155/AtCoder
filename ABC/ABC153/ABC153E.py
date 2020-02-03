h, n = map(int,input().split())
P = [list(map(int,input().split())) for i in range(n)]
a = 0
for i in range(n):
    if a < P[i-1][0] / P[i-1][1]:
        a = P[i-1][0]
        b = P[i-1][1]
        
while h > 0:
    h -= a
    ans += b
print(P[0][1])