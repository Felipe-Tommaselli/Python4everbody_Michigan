# Object Oriented Python

#! OBJECTS/INSTANCES: 

# objects: a bit of self-contained Code and Data
# ex: lists, strings, ints ...

#    ______                                                 ________
#  | input | <== objects interating between themselfs ==> | output |
#   ------                                                 --------

#! DEFINITIONS:

#* Class: a template
#* Method or Message: a defind capability of a class
#* Field or attribute: a bit of data in a class
#* Object or instance: a particular instance of a class

# Class é tipo o conceito de cachorro, o objeto é tipo um cachorro por si só,
# é possivel faazer carinho no objeto cachorro por exemplo
# São as habilidades do cachorro, tipo latir()

class PartyAnimal:
    x = 0

    def party(self):
        self.x += 1
        print('So far', self.x)

an = PartyAnimal()

an.party() # basicamente uma simplificação do de baixo (msm output)
PartyAnimal.party(an)

# type(an) retornara realmente a classe dele na forma '__main__.PartyAnimal
# dir(an) retornara as capabilities da classe (os metodos a serem usados)

print('type(an):', type(an))
print('dir(an)', dir(an))

# as coisas com __ __ pelo jeito sao coisas internas da classe

print('\n\n')
# * utilizamos os metodos constructors e destructors para criar e matar classes

class PartyAnimal2:
    x = 0
    
    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x += 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal2()

an.party()
an.party()
an = 42
print('an contains', an)

print('\n\n')

class PartyAnimal3:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x += 1
        print(self.name, 'party count', self.x)

    def __del__(self):
        print('I am destructed', self.x)

s = PartyAnimal3('Sally')
s.party()

j = PartyAnimal3('Jim')
j.party()
s.party()

print('\n\n')
#! Inheritance (herança):

class FootballFan(PartyAnimal3):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)

s = PartyAnimal3('Sally')
s.party()
# normal, ate agr

j = FootballFan('Jim')
j.party()
j.touchdown()

# como FootballFan "recebe" a classe partyanimal, é como se copiacemos tudo q ela faz
# e adicionacemos oq o fottball fan tbm faz. Resumindo, coisa de preguicoso, mas te 
# poupa de ter que copiar e colar tudo dnv do partyanimal no foottballfan
