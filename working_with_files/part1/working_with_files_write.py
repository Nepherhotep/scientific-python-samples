# encoding: utf-8

# открываем файл на запись
f = open("output.txt", 'w')

# пишем текст
f.write('hello, files!')

# добавляем символ переноса строки
f.write('\n')

# пишем втрую строку
f.write('hello again')

# обязательно закрываем файл
f.close()
