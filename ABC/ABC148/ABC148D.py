n = int(input())
A = list(map(int,input().split()))
ans = 0
x = 1

for i in range(n):
    if A[i-1] != x:
        ans += 1
    else:
        x += 1

if n == 1 and A[0] == 1:
    print("0")
elif  A == range(1, n+1):
    print("0")
elif x == 1:
    print("-1")
else:
    print(ans-1)