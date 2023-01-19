# ** 5. Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов. Негафибоначчи
# in                                           in
# 8                                            5
# out                                          out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21    5 -3 2 -1 1 0 1 1 2 3 5
n = int(input())
def fib(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
list = []
for i in range(n+1):
    list.append(((-1)**(i+1))*fib(i))
list.reverse()
for i in range(1, n+1):
    list.append(fib(i))
print(list)
