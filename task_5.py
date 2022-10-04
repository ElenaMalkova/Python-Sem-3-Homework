# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи] (https://ru.wikipedia.org/wiki/Негафибоначчи)

integer = int(input('Введите число: '))
list_of_fib = [0, 1]
limit = integer + 1

for i in range(2, limit):
    number_fib = list_of_fib[i - 1] + list_of_fib[i - 2]
    list_of_fib.append(number_fib)

for k in range(1, limit):
    number_fib = list_of_fib[-k] * -1
    list_of_fib.insert(k - 1, number_fib)

print(f'{list_of_fib}')
