n = list(map(int, input().split()))
mini = 1001
for i in n:
    if i > 0 and i < mini:
        mini = i
print(mini)