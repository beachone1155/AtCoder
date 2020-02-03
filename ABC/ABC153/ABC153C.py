n, k = map(int,input().split())
H = list(map(int,input().split()))

H.sort(reverse=True)

del H[0:k]
print(sum(H))