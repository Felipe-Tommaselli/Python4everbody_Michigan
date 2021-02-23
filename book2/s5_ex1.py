# contar quantas vezes cada palarva aparece em uma linha de um texto
 
counts = dict()
f = open(input("Nome do arquivo:"))
try:
    line = input("Linha:")
except:
    print("Invalid input")

words = line.split()
print('Words:', words)

print('\n')

for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)