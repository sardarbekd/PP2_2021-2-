list1 = list(map(str, input().split()))
list2 = []

for word in list1:
    list2.append(len(word))
max = -11111
for n in list2:
    if n>max :
        max = n
for word in list1 :
    if len(word)==max:
        print(word)
        break

print(max)