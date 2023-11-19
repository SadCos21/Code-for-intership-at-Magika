# Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.

list_numbers = list(map(int, input('Введите список чисел через пробел: ').split()))

for elem in list_numbers:
    if elem == 237:
        break
    elif elem % 2 == 0:
        print(elem)