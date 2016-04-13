# encoding: utf-8
# открываем файл на чтение
f = open("multiline_sample.txt")

for line in f.readlines():
    print(line)

f.close()