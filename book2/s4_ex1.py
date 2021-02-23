f = open(input("Enter file name: "))
list = list()

for line in f:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in list:
            list.append(word)

list.sort()
print(list)