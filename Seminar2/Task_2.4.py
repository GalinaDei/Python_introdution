 # * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20
a, b, N = int(input()), int(input()), int(input())
num_list = []
for i in range(-N, N + 1):
    num_list.append(i)
if a in num_list and b in num_list:
    num_prod = num_list[a - 1] * num_list[b - 1]
    print("-> ", num_list, "\n", "-> ", num_prod, sep="")
else:
    print("->", num_list, "#\n", "-> There are no values for these indexes!", sep="")