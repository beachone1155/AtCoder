N = int(input())

t_before = 0
x_before = 0
y_before = 0
ans = "Yes"
for i in range(N):
    t, x ,y = map(int,input().split())
    if abs(x - x_before) + abs(y - y_before) > t - t_before or (abs(x - x_before) + abs(y - y_before)) % 2 != (t - t_before) % 2:
        ans = "No"
        break

print(ans)