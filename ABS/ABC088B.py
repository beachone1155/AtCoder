n = int(input())
A = list(map(int,input().split()))
ans = 0
for i in range(n):
    if A == []:
        break
    ans += max(A)
    A.remove(max(A))
    if A == []:
        break
    ans -= max(A)
    A.remove(max(A))

print(ans)