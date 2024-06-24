my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0

while number < len(my_list):
    current_number = my_list[number]

    if current_number < 0:
        break

    if current_number == 0:
        number += 1
        continue

    print(current_number)
    number = number + 1
