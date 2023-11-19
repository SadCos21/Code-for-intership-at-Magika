# С помощью анонимной функции извлеките из списка числа, делимые на 15.

numbers = list(map(int, input('Введите список чисел через пробел: ').split()))
result = list(filter(lambda x: x % 15 == 0, numbers))
print(result) 