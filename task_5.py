# Найдите три ключа с самыми высокими значениями в словаре 

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
result = {}
max_value = sorted(my_dict.values(), reverse= True)[:3]
for i in range(3):
    for k in my_dict:
        if my_dict[k] == max_value[i]:
            result[k] = max_value[i]

print(result)