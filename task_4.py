# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

integer = int(input('Введите число: '))

def convert_to_bin(intgr):
    bin_num = []
    while True:
        digit = intgr % 2
        bin_num.append(digit)
        intgr //= 2
        if intgr == 0:
            break
    result = ''
    bin_num.reverse()
    for i in bin_num:
        result += str(i)
    return result


print(f'{convert_to_bin(integer)}')
