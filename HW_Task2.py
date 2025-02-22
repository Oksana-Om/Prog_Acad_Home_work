# Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
import re

def validation(card):
    pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
    match = re.findall(pattern, card)
    if match:
        print("Your card with number ", match, "is validated")
    else:
        print("Your card has not been verified")

card = input("input card's number: ")
validation(card)
