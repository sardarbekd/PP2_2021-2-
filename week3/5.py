n = list(map(int, input().split()))
m = []
for i in range(len(n)):
    if n[i] != 0:
        m.append(n[i])
for i in range(len(n) - len(m)):
    m.append(0)
print(*m)