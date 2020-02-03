N = int(input())
P = list(map(int,input().split()))	

result = 0

for i in range(N):
    
    for j in range(i):

        for k in range(j):
            if P[j-1] > P[k-1]:
                break
            result = result + 1

print(result)
    

