n = list(map(int, input().split()))
cnt = 0
for i in range(len(n) - 1):
    for j in range(i + 1, len(n)):
        if n[i]==n[j] and i<j :
            cnt += 1

print(cnt)
        