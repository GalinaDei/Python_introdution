# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in                                             in
# Number of words: 10                            Number of words: -1
# out                                            out
# авб абв бав абв вба бав вба абв абв абв        The data is incorrect
# авб бав вба бав вба

import random


def text_creater(number):
    abc = ["абв","бав","вба", "ааа", "ббв", "абв", "баа"]
    str = [''.join(random.choice(abc)) for i in range(number)]
    print(str)
    return str


text = text_creater(int(input()))

str = list(filter(lambda x: x != "абв", text))
print(str)
