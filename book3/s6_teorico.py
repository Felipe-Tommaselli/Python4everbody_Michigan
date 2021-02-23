# JSON (JavaScript Object Notation)

# JSON mais facil que XML

import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 302 859 0209"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data) # info é um dict
print(info)

print('Name:', info["name"]) 
# info["name"] é um elemento do dict info na tag "name"
print('Hide:', info["email"]["hide"])
# info["email"] é outro dict dentro do dict info, "hide é uma tag de info["email"] 

# ! (SOA) Service Oriented Approach and API (Application Programming Interface)

# A função de uma API é, basicamente, facilitar e simplificar o trabalho de
# desenvolvedores, além de oferecer um padrão para a criação de novas plataformas.

# mais comum ser consumidor de API doq desenvolvedor 

