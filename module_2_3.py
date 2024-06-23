my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

number = 0

while number < len(my_list):
    number2 = my_list[number]
    if number2 < 0:
        break
    print(number2)
    number = number + 1
