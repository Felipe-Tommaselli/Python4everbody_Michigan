# data on the Web

# w/ the HTTP request/response cicle a agreeing format of sending data 
# was created, a road between two aplications: the Wire Format

# *  _______________  serialize                de-serialize  ______________
# * | py dictionary |   ==>    XML/JSON format      ==>    | Java HashMap |
# * ----------------                                       ---------------

# XML é mais velho e mais dificil que o JSON, os dois são padronizados

# ! XML (eXtensible Markup Language)

# * Simple Element
# ! Complex Element
#
# <people>
#    <person>
# *      <name>Chuck</name>
# *      <phone>303 4456</phone>
#    </person>
# !  <person>
# !     <name>Noah</name>
# !     <phone>622 7421</phone>
# !  </person>
# </people>


# ! BASICS

# # Start Tag
# * End Tag
# ! Text Content
# ? Attribute
# (fico ruim, abrastrai ae)

# ! Terminology

#  Tags: indicate the begining and ending of elemtns
#* Attributes: Keyword/value pairs on the opening tag of XML
#  Serialize/ De-Serialize: Convert data in one program into a common format
#  that can be stored and/or transmitted between systems in a programming 
#  language-independent manner

# ! XML SCHEMA

# um contrato para validar o formato do XML enviado e recebido para que
# ambos estejam de acordo (meio que um esqueletão ja preparado). 
# Para isso ha um XML Validator

# ! XML Schema languages

# W3C Schema (mais comum)

# ! parsing XML

import xml.etree.ElementTree as ET

# library to parse XML

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text) # text
print('Attr:', tree.find('email').get('hide')) # attribute

# se a arvore é muito longa:

input = '''<stuff>
    <users
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
list = stuff.findall('users/user')
print('user count:', len(list))

for item in list:
    print('Name:', item.find('name').text) # text
    print('Id:', item.find('Id').text) # text    
    print('Attr:', item.get('x')) # attribute
