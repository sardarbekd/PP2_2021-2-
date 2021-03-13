n = int(input())
d = dict()
for i in range(n):
    list1 = list(map(int, input().split()))
    d[i] = sum(list1)
k = int(input())
ans = sorted(d.items(), key = lambda x : x[1])
j = 0
kol = []
for i in ans:
    if j<k:
        kol.append(i[0])
        j+=1
print(kol)

    