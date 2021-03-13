import re
file = open('file.txt', 'r', encoding = 'utf-8')
file.read()
txt = r'\nФилиал.+<?Pnamecompany>.+'
nameOfCompany = re.search(txt, file).group('namecompany')
print(nameOfCompany)