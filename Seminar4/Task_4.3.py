# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности в том же порядке.
# in                           in
# 7                            -1
# out                          out
# [4, 5, 3, 3, 4, 1, 2]        Negative value of the number of numbers!
# [5, 1, 2]                    []
import random
from collections import Counter


def num_sequence(num):
    new_list = []
    if num < 0:
        print("Negative value of the number of numbers!")
    else:
        for i in range(1, num + 1):
            num1 = random.randint(0, 9)
            new_list.append(num1)
        print(new_list)
    return new_list


def non_repeating_elements(num_list):
    list2 = []
    list1 = Counter(num_list)
    for k, v in list1.items():
        if v == 1:
            list2.append(k)
    print(list2)


array = num_sequence(int(input()))

non_repeating_elements(array)
