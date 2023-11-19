#Нужно проверить, все ли числа в последовательности уникальны.

numbers = list(map(int, input('Введите список чисел через пробел: ').split()))
print(len(numbers) == len(set(numbers)))