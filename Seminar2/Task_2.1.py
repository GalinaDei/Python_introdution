# # 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27
from decimal import Decimal
num = Decimal(input())
num_sum = 0
while num % 1 != 0:
    num = num * 10
num = int(num)
while num > 0:
    num_sum += num % 10
    num //= 10
print(num_sum)

