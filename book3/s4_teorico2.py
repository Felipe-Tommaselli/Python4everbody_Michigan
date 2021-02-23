# devido ao game changind da urllib, vamos dar uma separada nas coisas

import urllib.request, urllib.parse, urllib.error

# uma houtra boa e facil é (pena que não funcionou)
# import requests

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# funciona como um f = open()

for line in fhand:
    print(line.decode().strip())

# só pensar como se fosse um file, por exemplo

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# igualzinho nos files, só muda o open e depois disso o decodificar


# ! web scrape or web spidering
    # < https://pt.wikipedia.org/wiki/Coleta_de_dados_web >
    # < https://pt.wikipedia.org/wiki/Rastreador_web >
# (maybe illegal) 

# HTML é feio e adimite mtos errosde sintaxe, por isso pode dar mto problema na
# hora de fazzer buscas, envovendo mta manipulação de strings e etc

# * pra isso temos a software library 'BeautifulSoup' do www.crummy.com
# < https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_installation.htm >

from bs4 import BeautifulSoup

html = urllib.request.urlopen(input('Enter - ')).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

# colocar uma pagina como input e ela vai te dar de volta todas as tags da pag
# pode por http://www.dr-chuck.com/page1.htm e ele vai voltar só uma tag msm

