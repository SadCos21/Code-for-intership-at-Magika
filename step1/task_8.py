# Напишите проверку на то, является ли строка палиндромом. 
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.

def palindrom(text):
    text = text.replace('.','').replace(',','').replace(' ','').lower()
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]: 
            return False
    return True

text = input('Введите строку: ')
print(palindrom(text))
