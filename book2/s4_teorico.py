# listas (mutaveis)

friends = ['joseph', 'carl', 'noah']

for friend in friends: 
    print('Hello', friend)

# strings não são listas (são tuplas)

# função range(), retorna uma lista conforme os numeros

print(range(7))


# temos como organizar elas ainda
friends.sort()
print(friends)

# não sejapreguiçoso

print([1, 5, 9, 0, -4, 66].sort()) # printa None
list = [1, 5, 9, 0, -4, 66]
list.sort()
print(list)

# não esquecerdo max min sum e len

print("\naverage of list =", sum(list)/len(list))
print("list max =", max(list))

# um jeito bom de trabalhar com manipulações de strings é
 
string = "with three words"
s = string.split()
print(f'\n{string}')
print(s)
s[1] = 'two'
print(s)

# split é esperto

string_ruim = "without-tree-words"
s2 = string_ruim.split('-')
print(string_ruim)
print(s2)