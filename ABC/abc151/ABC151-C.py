N,M =  map(int,input().split())
WA = 0
AC = 0
for i in range(M):
    p,S = input().split()
    
    if S =="WA":
        WA = WA + 1
    if S == "AC":
        AC = AC +1
        for i in range(M):
            p1,S1 = input().split()
            if p != p1:
                break
print(S)