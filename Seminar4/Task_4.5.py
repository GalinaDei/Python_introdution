# ** 5. Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл,
# содержащий сумму многочленов.
# in                                                                          in
# "poly.txt"                                                                  "poly.txt"
# "poly_2.txt"                                                                "poly_2.txt"
# out in the file                                                             out
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0   The contents of the files do not match!
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
#
# in
#
#
#
# out
# The contents of the files do not match!

def file_writer(file_name1, file_name2):
    with open(file_name1, 'r') as input0, open(file_name2, 'r') as input1:
        for line in input0:
            line1 = input0.readlines()
        for line in input1:
            line2 = input1.readlines()
        with open("poly2.txt", "a", encoding="UTF-8") as third_f:
            for i in range(len(line2)):
                # for j in range(len(line1)):
                third_f.write(line1[i].replace("= 0\n", "+ "))
                third_f.write(line2[i])
    return


file_writer('poly.txt', 'poly1.txt')
