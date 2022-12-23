# 5. Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099
from math import*
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
distance = sqrt((x1-x2)**2+(y1-y2)**2)
print("in", x1, y1, x2, y2, "out", distance, sep="\n")