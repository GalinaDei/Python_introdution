# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
# предыдущего элемента. Use comprehension.
# in                                   in
# 9                                    10
# out                                  out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]       [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [16, 3, 7, 10]                       [24, 15, 23, 25]

import random

def list_create(num):
    if num.isdigit() and int(num) > 1:
        lst = [random.randint(0, 100) for i in range(int(num))]
        return lst
    else:
        print("Введено екорректное значение")

lst = list_create(input("Введите число > 2:  "))
print(lst)

def bigger_value_list(list):
    if list:
        lst = [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]
        print(lst)

bigger_value_list(lst)
