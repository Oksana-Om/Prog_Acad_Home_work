# Напишіть функцію, яка перевіряє правильність логіну.
# Правильний логін – рядок від 2 до 10 символів, що містить лише літери та цифри.

import re

def validation_of_login(login):
    pattern = r'^[A-Za-z0-9]{2,10}$'
    match = re.findall(pattern, login)
    if match:
        print("Your login is correct")
    else:
        print("Mistake in your login")

login = input("input your login: ")
validation_of_login(login)
