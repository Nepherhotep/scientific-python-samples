# encoding: utf-8
# открываем файл на чтение
f = open("multiline_sample.txt")

# проходим по всем строкам
for line in f.readlines():
    print(line)
