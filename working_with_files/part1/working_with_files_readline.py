# coding: utf-8

f = open("multiline_sample.txt")

result = 0

line = f.readline()
while line:

    # конвертируем строку в число, и добавляем его к сумме
    result += int(line)

    # читаем следующую строку
    line = f.readline()

# выводим результат в консоль
print(result)
f.close()
