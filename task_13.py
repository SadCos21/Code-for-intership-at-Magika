# При заданном целом числе n посчитайте n + nn + nnn

n = int(input('Введите число n: '))
print(n + int(str(n)*2) + int(str(n)*3))