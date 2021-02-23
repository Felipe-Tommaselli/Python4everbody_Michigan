# Networked Tecnology

# *  ______________     networking     ______________
# * | application |       <==>        | application |
# * --------------                    --------------


# the <========> is called 'socket' (TCP connections)
# internet can be a socket

# A 'port' is an application-specific software communications endpoint (TCP connections)
# é tipo as portas do Monstros SA

# python como sempre ja ajuda nois, ele ja tem um suporte pra TCP sockets 

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# host: data.pr4e.org
# port: 80

# até o momeento apenas foi efetuada a conexão entre as duas aplicações
# p/ garantir q a comunicação seja padronizada e eficiente há protocolos

# ! HTTP (Hypertext Transfer Protocol)
# A set of protocols/rules that all the communications uses

# vamos pra um programa mais real

# *  ______________     socket          ,_________________
# * | my computer |================(Port 80) www.py4e.com |
# * --------------                     '-----------------

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1): # EOF
        break
    print(data.decode())
mysock.close()

# we kinda send a request of some data, than when we recieve we print it

# PLUS: HOW INTERNET WORKS < http://www.net-intro.com/ >