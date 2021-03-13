import re
file = open('file.txt', 'r', encoding = 'utf-8')
file.read()
x = re.findall("^Филиал", file)
print(x)