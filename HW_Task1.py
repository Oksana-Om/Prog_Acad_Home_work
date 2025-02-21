#Напишіть регулярний вираз, який знаходитиме в тексті фрагменти,
# що складаються з однієї літери R, за якою слідує одна або більше літер b,
# за якою одна r. Враховувати верхній та нижній регістр.

import re
string = 'xdfkh hjRbbr hhk Rbrb Rbbbbbrbnj'
pattern = r'[R]{1}[b]{1,}[r]{1}'
match = re.findall(pattern, string)
if match:
    print(match)
else:
    print("pattern not found")