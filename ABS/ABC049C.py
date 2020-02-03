S = input()

S = S.replace("eraser","0")
S = S.replace("dreamer","0")
S = S.replace("erase","0")
S = S.replace("dream","0")
S = S.replace("0","")

if len(S) == 0:
    print("YES")
else:
    print("NO")
