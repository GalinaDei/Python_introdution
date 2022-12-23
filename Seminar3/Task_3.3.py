# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции
# преобразования, без строк.
# in                  in
# 88                  11
# out                 out
# 1011000             1011
def binary_num_converter(num1):
    num_list = []
    while num1:
        num_list.append(num1 % 2)
        num1 //= 2
    num_list.reverse()
    return num_list


def num_printer(array):
    for i in range(len(array)):
        print(array[i], end="")
    return


num = binary_num_converter(int(input()))
num_printer(num)