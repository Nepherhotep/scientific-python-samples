# encoding: utf-8
# открываем файл на чтение
my_file = open("sample.txt")

# читаем файл
file_content = my_file.read()

# закрываем файл
my_file.close()

# печатаем результат в консоль
print(file_content)
