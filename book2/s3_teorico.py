# files

file = open("words.txt")

# file não é o texto dentro do arquivo, é apenas um handle do arquivo no
# programa, que acaba ajudando na roda de ler e etc
print(file)

# quando fazem isso, ai sim colocamos na varaivel inp o texto do arquivo
inp = file.read()

print(inp)


# quando lemos um arquivo cada linha tem um \n ja, o que acontece quando
# printamos é que ele acabara jogando uma linha a mais, para isso:

for line in file:
    line = line.rstrip() # assim q tiramos o \n a mais
    print(line)

# um jeito bom de ler os arquivos pulando aslinhas "inuteis" é:

for line in file:
    line = line.rstrip() # assim q tiramos o \n a mais
    if not line.startswith('From:'):
        continue
    print(line)

file.close()