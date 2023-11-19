# Напишите программу, которая принимает текст и выводит два слова: 
# наиболее часто встречающееся и самое длинное.

text = input('Введите текст: ')
list_text = text.replace(',','').replace('.','').lower().split()
frequent = ''
max_len = ''

for elem in list_text:
    if list_text.count(elem) > list_text.count(frequent):
        frequent = elem
    if len(elem) > len(max_len):
       max_len = elem

print(f'Самое частое слово: {frequent}. Самое длинное слово: {max_len}') 