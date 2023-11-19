# Нужно вывести первые n строк треугольника Паскаля.
from math import factorial

def bin_сoef(k, n):
    return int(factorial(n)/(factorial(n-k) * factorial(k)))

n = int(input('Введите число n, до какой строки хотите видеть треугольник Паскаля: '))

for i in range(1,n+1):
    print((n - i) * ' ', end= '')
    for j in range(i):
        print(bin_сoef(j, i-1), end= ' ')
    print() 
