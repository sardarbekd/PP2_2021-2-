

n = list(map(int, input().split(".")))


if 1899<=n[2]<=1922:
    if 1<=n[1]<=12:
        if 1<=n[0]<=31:
            print("YES")
                
else:
    print("NO")