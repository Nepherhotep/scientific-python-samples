# coding: utf-8

f = open("multiline_sample.txt")

result = 0

line = f.readline()
while line:
    # конвертируем строку в число
    value = int(line)

    # добавляем число к сумме
    result += value

    line = f.readline()

# выводим результат в консоль
print(result)
f.close()
