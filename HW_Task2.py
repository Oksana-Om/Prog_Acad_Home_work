# Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).

import re

string = input("input card's number: ")

pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
match = re.findall(pattern, string)
if match:
    print("Your card with number ", match, "is validated")
else:
    print("Your card has not been verified")
