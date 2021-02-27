txt = str(input())
s = str(input())
x = txt.find(s)
if x != -1 :
    print("First time", s, "occured in position", x)
else:
    print("Not found")
