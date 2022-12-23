# 1. Задайте список, состоящий из произвольных чисел, количество задаёт
# пользователь. # Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётных позициях(не индексах).
# in                        in
# 5                         4
# out
# [10, 2, 3, 8, 9]          [4, 2, 4, 9]
# 22                        8
from random import sample


def odd_sum_counter(num):
    new_list = sample(range(1, num * 2), num)
    print(new_list)
    counter = 0
    for i in range(0, len(new_list) , 2):
        counter += new_list[i]
    return counter


print(odd_sum_counter(int(input())))