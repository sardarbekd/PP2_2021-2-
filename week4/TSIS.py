from re import *
with open("file.txt", "r", encoding="utf-8") as f:
    text_line = " ".join(f.readlines())

name_of_company = search(r"ДУБЛИКАТ\n (.+)\n", text_line).group(1)
BINnumber = search(r"БИН (\d+)\n", text_line).group(1)
items = findall(r"\d+\.\n([^\n]+)\n([0-9, ]+) x ([0-9, ]+)\n([0-9, ]+)", text_line)
date = search(r"Время: ([^\n]+)\n", text_line).group(1)
adress = search(r"г\. ([^\n]+)\n", text_line).group(0)
print(f"Name of the company: {name_of_company}")
print(f"BIN number: {BINnumber}")

for index, item in enumerate(items):
    print(f'{index}. {item[0]}')
    print(f'\t{item[1]} * {item[2]} = {item[3]}')

print(f'Date: {date}')
print(f'Adress: {adress}')
