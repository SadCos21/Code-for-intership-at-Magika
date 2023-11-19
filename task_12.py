# Напишите программу, которая принимает имя файла и выводит его расширение. 
# Если расширение у файла определить невозможно, выбросите исключение.
string = 'kek.'
lst = string.split('.')
print(len(lst))

name_file = input('Введите имя файла:')
parts = name_file.split('.')
if (len(parts) != 2) or (parts[0] == '') or (parts[1] == ''):
    raise ValueError('Расширение определить невозможно')
else: 
    print('Расширение файла:', parts[1])
# pathlib