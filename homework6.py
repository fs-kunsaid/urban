# Словарь
my_dict = {'Max': 1987, 'Fedor': 1978, 'Ben': 1956}
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Elena', 'Такого значения нет'))
my_dict.update({'Elena': 1945, 'Ivan': 1990})
print(my_dict)
my_dict.pop('Ben')
print(my_dict)
# Множество
my_set = {5, 8, 13, 21, True, 8, 21, False, 13, 34}
print(my_set)
my_set.update({55, 89})
my_set.add(144)
print(my_set)
my_set.discard(3)
my_set.remove(34)
print(my_set)


