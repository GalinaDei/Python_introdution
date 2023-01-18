#  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся
#  в отдельных текстовых файлах.
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
#
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

def file_coder(file):
    with open(file, 'r') as fr:
        for s in fr:
            str1 = s.strip()
            print(str1)
            big_array = []
            count = 0
            for i in range(len(str1) - 1):

                if str1[i] == str1[i + 1]:
                    count += 1

                elif str1[i] == str1[i + 1] and (i + 1) == -1:
                    count += 1

                elif str1[i] != str1[i + 1]:
                    count += 1
                    big_array.extend((str(count), str1[i]))
                    count = 0

            if str1[i] == str1[-1]:
                count += 1
                big_array.extend((str(count), str1[i]))
            else:
                big_array.extend(("1", str1[-1]))

            with open("text_code_words", "a") as fc:
                for c in big_array:
                    fc.write(c)
                fc.write("\n")


def file_decoder(file):
    with open(file, "r") as fdc:
        for line in fdc:
            str = line.strip()

            text = []
            num = ""
            for c in str:
                if c.isdigit():
                    num += c
                else:
                    text.append(c * int(num))
                    num = ""
            with open("file_decode_words.txt", "a") as fd:
                fd.writelines(c for c in text)
                fd.write("\n")


file_coder('text_word.txt')
file_decoder("text_code_words")

