a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
diff = (b1*3600 + b2*60 + b3) - (a1*3600 + a2*60 + a3)
print(diff)