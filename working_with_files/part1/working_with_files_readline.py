f = open("multiline_sample.txt")

line = f.readline()
while line:
    print(line)
    line = f.readline()

f.close()