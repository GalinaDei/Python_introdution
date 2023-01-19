# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
from decimal import *


def accuracy_config (mess: str):
    num = Decimal(mess)
    d = input("Enter the required accuracy '0.0001': ")
    new_num = Decimal(num).quantize(Decimal(d))
    print(new_num)
    return new_num


accuracy_config (input("Enter a real number: "))
