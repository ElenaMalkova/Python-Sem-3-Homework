# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [1, 3, 5, 10, 2, 4, 1]
my_mul = 0
my_mul__list = []
index = 0
last_index = len(my_list) - 1
while index <= last_index / 2:
    my_mul = my_list[index] * my_list[last_index - index]
    my_mul__list.append(my_mul)
    index += 1
print(f'В списке {my_list}\nсумма крайних элементов: {my_mul__list}')