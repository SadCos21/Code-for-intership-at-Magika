# Отсортируйте словарь по значению в порядке возрастания и убывания.

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# По возрастанию
sort_v = sorted(zip(d.values(),d.keys()))
sort_d = {elem[1]: elem[0] for elem in sort_v}
print(sort_d)

# По убыванию
sort_v = sorted(zip(d.values(),d.keys()), reverse = True)
sort_d = {elem[1]: elem[0] for elem in sort_v}
print(sort_d)