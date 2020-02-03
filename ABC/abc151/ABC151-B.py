#K点満点という条件を見逃した

N,K,M =  map(int,input().split())
A =  list(map(int,input().split()))

result = N*M - sum(A) 
if result >K:
    print("-1")
elif result <=0:
    print("0")
else:
    print(result)