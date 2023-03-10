# * 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10)
# многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in                                                         in
# 9                                                          0
# 5                                                          -1
# 3                                                          4
# out in the file                                            out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0      3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0                              4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0                                              4*x^2 - 4 = 0
#                                                            2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0
import random


def polynomial_to_file(num):
    for i in range(num, 0, -1):
        k = random.randint(0, 10)
        s = random.choice("+-")
        with open("poly1.txt", "a", encoding="UTF-8") as my_f:
            if k != 0:
                my_f.write(f"{k}*x^{i} {s} ")
    k = random.randint(0, 10)
    with open("poly1.txt", "a", encoding="UTF-8") as my_f:
        my_f.write(f"{k} = 0\n")
    return


for i in range(3):
    polynomial_to_file(int(input()))
