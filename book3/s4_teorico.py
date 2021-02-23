# Unicode characteres and strings

# Tabela ASCII

print(ord('H'))
print(ord('h'))

# por isso que letras maiusculas são maiores que minusculas

print(ord('\n'))

# para garantir que o pc do EUA e da china tenham a mesma base de caracteres,
# foi criado o UNICODE < https://pt.wikipedia.org/wiki/Unicode >

# no python3:

print(type('abc')) # string
print(type(b'abc')) # bytes
print(type(u'abc')) # unicode

# todas as strings são convertidas pra unicode, portanto não faz diferença usar o u
# o byte faz diferença, ele armazena tudo em bytes

# quando vamos enviar dados por socket, enviamos bytes
# para isso é necessario que o python encode essas strings unicode para bytes

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # encode
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode()) # decode


# quando vamos enviar algum dado em formato de string precisamos passa-lo para bytes
# depois podemos voltar para string normalmente através do decode

# para o teste vamos rodar o programa agora sem o decode, fica tudo desformatado e estranho
    
    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
    print(data)
mysock.close()

# quando dizemos encode() ele assumi que queremos encode(UTF-8), que é o unicode

# recv() sempre devolve em bytes, que é oq o socket entende
# quando vamos enviar com o send() tambem é necessaria sempre lemvrar do encode


# * VOCE ACHA QUE TA FACIL COM O SOCKET? ENTÃO ESPERA QUE O PYTHON TE CARREGA

# e vamos de URLLIB

import urllib