# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности в том же порядке.
# in                           in
# 7                            -1
# out                          out
# [4, 5, 3, 3, 4, 1, 2]        Negative value of the number of numbers!
# [5, 1, 2]                    []
import random
from collections import Counter

def non_repeating_elements(num):
    new_list = []
    for i in range(1, num+1):
        num1 = random.randint(0, 9)
        new_list.append(num1)
    print(new_list)
    list2 = Counter(new_list)
    print(list2.value(1))

    return list2



print(non_repeating_elements(int(input())))



