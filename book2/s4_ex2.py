fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

list = list()
f = open(fname)
count = 0
for line in f:
    line = line.rstrip()
    list = line.split()
    if list == []: continue
    elif list[0].lower() == 'from':
        count += 1
        print(list[1])

print("There were", count, "lines in the file with From as the first word")