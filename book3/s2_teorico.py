# Regular expressions

# tipo um jeito melhro e esperto de procurar e fazer coisas, "wild card"

# quick guide in "s1_teorico_img.png" ou em 'https://docs.python.org/3/howto/regex.html'

import re

# re.search() , parecido com o find()

# re.findall(), parecido com a combinação do find() com slicing [:]

# exemplo sem o re:

f = open('mbox-short.txt')
for line in f:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

# com o re:

for line in f:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

# mais um exemplo usando o ^ agora, primeiro vamos ver a forma que ja conhecemos:
print('\n\n\n')
for line in f:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
# com a regular expression:

for line in f:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

# Algo muito louco, é procurar emails na forma 'X-blabla: ...' na lista

print('\n\n\n')
for line in f:
    line = line.rstrip()
    if re.search('^X.*:', line):
        print(line)

# '^' match the start of the line
# '\' match any nn-whitespace character
# '+' one or more times
# '.' match any character
# '*' many times
# '?' non-greedy

string = 'My 2 favorite number are 19 and 42'

print(re.findall('[0-9]+', string))

# procurando os numeros entre 0 e 9 +, ou seja todos e adicionando a uma lista


# printar apenas o email
msg = 'From david.horwitz@uct.ac.za Fri Jan  4 04:33:44 2008'

print(re.findall(r'\S+@\S+', msg))