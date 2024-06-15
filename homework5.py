immutable_var = 1, 2, 3, 4, 5, 'слово', True, 2.5
print(immutable_var)
print(type(immutable_var))
# immutable_var[3] = 10

mutable_list = [1, 2, 3, 4, 5, 'слово', True, 2.5]
print(mutable_list)
print(type(mutable_list))
mutable_list[3] = 10
print(mutable_list)
mutable_list[5] = False
mutable_list[6] = 'слово2'
print(mutable_list)
