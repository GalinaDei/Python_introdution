# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн
# in                   in
# 54                   9990
# out                  out
# [2, 3, 3, 3]         [2, 3, 3, 3, 5, 37]
def prime_factors_search (num):
    spisok = []
    for i in range(2, num+1):
        while num % i==0:
            spisok.append(i)
            num=num/i
    return spisok


print(prime_factors_search (int(input())))
