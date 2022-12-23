# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# in                                          in
# 5                                           3
# out                                         out
# [5.16, 8.62, 6.57, 7.92, 9.22]              [9.26, 8.5, 1.14]
# Min: 0.16, Max: 0.92. Difference: 0.76      Min: 0.14, Max: 0.5. Difference: 0.36
from random import sample


def list_creater(num):
    new_list = sample(range(100, 999), num)
    for i in range(len(new_list)):
        new_list[i] = new_list[i] / 100
    return new_list


def residual_diff(new_list):
    max_resid = 0.00
    min_resid = 0.99
    for i in range(len(new_list)):
        if new_list[i] - int(new_list[i]) > max_resid:
            max_resid = new_list[i] - int(new_list[i])
        if new_list[i] - int(new_list[i]) < min_resid:
            min_resid = new_list[i] - int(new_list[i])
    difference = max_resid - min_resid
    list0 = [round(min_resid, 2), round(max_resid, 2), round(difference, 2)]
    return list0


array = list_creater(int(input("Введите число: ")))
list0 = residual_diff(array)
print(array)
print(f"Min: {list0[0]}, Max: {list0[1]}, Difference: {list0[2]}.")
