s = list(map(int, input().split()))
sum1 = 0
for i in s:
    if s.count(i) == 1:
        sum1 += i
print(sum1)