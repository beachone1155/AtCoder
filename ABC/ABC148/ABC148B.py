n = int(input())
li = list(input())
ans = ""
for i in range(n):
    ans += li[i] + li[i+n+1]
print(ans)

