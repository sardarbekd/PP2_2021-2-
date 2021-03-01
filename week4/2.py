import re
manual = "[a-ZA-z0-9] + @[a-zA-Z] + \.[net|com|edu|kz]"
users_input = input()
if(re.search(manual, users_input)):
    print("valid email")
else:
    print("invalid email")