import math
 
a,b,h,m = map(int,input().split())
 
sita = 0.5 * (h*60 + m)
fai = 6*m
print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(sita) - math.radians(fai))))
