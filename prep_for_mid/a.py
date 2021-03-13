n = list(map(int, input().split(".")
wet = 0
for i in range(3):
    if i == 0:
        if 1<=n[i]<=31:
            wet=0
        else: wet = 1
    elif i == 1:
        if 1<=n[i]<=12:
            wet=0
        else:
            wet=1
    else:
        if  1299<=n[i]<=1922:
            wet=0
        else:
            wet=1

if wet == 0:
    print("YES")
else:
    print("NO")
