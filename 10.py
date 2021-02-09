k , n = map(int , input().split())
stranica = int(n/k) + 1
if stranica==1:
    stroka = n
else:
    stroka = n % k
    
print(stranica , stroka)