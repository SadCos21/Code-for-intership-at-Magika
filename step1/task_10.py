# Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.

numbers = input('Введите последовательность чисел через запятую: ')
list_numbers = list(map(int, numbers.split(',')))
tuple_numbers = tuple(list_numbers)
print('Список:', list_numbers)
print('Кортеж:', tuple_numbers)
