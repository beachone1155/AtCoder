n = int(input())
A = list(map(int,input().split()))
ans = "APPROVED"

for i in range(n):
    if A[i] % 2 == 0:
        if A[i] % 3 != 0 and A[i] % 5 != 0:
            ans = "DENIED"

print(ans)