# Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
# Вимоги:
# -Цифри (0-9).
# -лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
# -у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
# -Символ "-" не може повторюватися.

import re

string = input("input your mail: ")

def validation_of_email(email):
    pattern = r'^[A-Za-z0-9][A-Za-z0-9_-]*[A-Za-z0-9]$'
    patt2 = r'[-]{2,}|[_]{2,}'
    match = re.findall(pattern, string)
    mistake = re.findall(patt2, string)
    if match and not mistake:
        print("Your email ", match, "is validated")
    else:
        print("Mistake in your email")

validation_of_email(string)

