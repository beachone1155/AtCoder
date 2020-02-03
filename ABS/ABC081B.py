n = int(input())
A = list(map(int,input().split()))

def calc_surplus(n):
    return n % 2

def calc_half(n):
    return n / 2

result = 0

for i in A:
    A_surplus = list(map(calc_surplus, A))
    if 1 not in A_surplus:
        A = list(map(calc_half,A))
        result = result + 1
    else:
        break

print(result)