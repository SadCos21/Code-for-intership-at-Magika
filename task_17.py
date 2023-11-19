# Сложите цифры целого числа
number = int(input('Введите целое число: '))
string_number = str(number).replace('-','')
s = 0
for chr in string_number:
    s += int(chr)
print('Сумма цифр числа:', s)