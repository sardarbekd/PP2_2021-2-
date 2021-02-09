d = int(input())
m = d * 2 # 360gradusov 12h 720min -> per degree=2min 
h = int(m/60)
m = m % 60
print("It is", h , "hours", m , "minutes.")