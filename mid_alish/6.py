a = list(map(int,input().split()))
n = int(input())
absent = []
for i in range(1, max(a) ):
    if i in a:
        continue
    if i not in a:
        absent.append(i)
    i += 1
print(absent[n-1])
