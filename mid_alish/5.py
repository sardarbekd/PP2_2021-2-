a = list(map(int, input().split()))
b = list(map(int, input().split()))
list1 = []

for i in a:
    for j in b:
        if i not in b and j not in a:
            list1.append(i)
            list1.append(j)
list1 = sorted(list1)
print(*list1)