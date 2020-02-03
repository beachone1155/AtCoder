n,a,b = map(int,input().split())
N = list(range(1,n+1))
ans = 0

def digitSum(n):
    s = str(n)
    array = list(map(int, s))
    return sum(array)

for i in N:
    if a <= digitSum(i) and digitSum(i) <= b :
        ans += i

print(ans)
