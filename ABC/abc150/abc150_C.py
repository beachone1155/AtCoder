import itertools

N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

r = list(itertools.permutations(range(1,N+1)))

print(abs(r.index(P)-r.index(Q)))