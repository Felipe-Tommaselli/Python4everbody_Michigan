import re

f = open(input('Enter name of the file: '))

sum = 0
for line in f:
    line = line.rstrip()
    for num in re.findall('[0-9]+', line): sum += int(num)

print('sum =', sum)