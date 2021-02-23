name= input("Enter file name: ")
fh = open(name)
for line in fh:
    #line = line.rstrip()
    for letter in line:
        letter = letter.upper()
        print(letter, end='')
fh.close()

# ou
print("\n=-=-=-=-=-=-=-=-=-=-=-=\n")

fh2 = open(name)
for line2 in fh2:
    line2 = line2.rstrip()
    print(line2.upper())
fh2.close()