# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in                  in
# 4                   5
# out                 out
# [2, 5, 8, 10]       [2, 2, 4, 8, 8]
# [20, 40]            [16, 16, 4]
from random import sample


def list_creater(num):
    new_list = sample(range(1, num * 2), num)
    return new_list


def digit_pair_product_counter(array):
    new_list = []
    for i in range(0, len(array) // 2):
        if len(array) % 2 == 0:
            new_list.append(array[i] * array[-1 - i])
        else:
            new_list.append(array[i] * array[-1 - i])
    if len(array) % 2 != 0:
        new_list.append(array[len(array) // 2])
    return new_list


sum_list = list_creater(int(input()))


print(sum_list)
print(digit_pair_product_counter(sum_list))
