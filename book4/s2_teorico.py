# Using Databases with Python

#! Relational databases

# relational databases model data by storing rows and colunms in tables.
# The power of the Relat. Databases lies in its ablity to efficiently retrieve data from
# those tables in particular where tgere are multipe tables and the relationships 
# betwenn those tables involved in the query.

#* DATABASE: Contains many tables
#* RELATION (OR TABLE): Contains tuples and attributes
#* Tuple (or row): A set of fields that generally represents and "objects" like a person or a music track
#* Attribute (also column or field): One of possibly many elements of data corresponding
    #* to the object represented by the row

#    Attribute (column)
#      -^-
#   [ ][ ][ ][ ]
#   [ ][ ][ ][ ]
#   [ ][ ][ ][ ] } Tuple (row)
#   [ ][ ][ ][ ] 
#  |___  _______|
#      \/
#    Relation (table)


#! SQL (Structured Query Language)

# A lingaugem usada para comandar o banco de dados (de forma eficiente)
# como: criar uma tabela, pegar dados, iserir dados, deletar dados etc

#  -----  SQL  -----------       ---------------
# | We | <==> | Database | <==> | ****Data**** |
# -----       -----------       ---------------

# Muito mais facil trabalhar com uma database do que diretamente com os dados.
# Os databases são uma especie de API, a qaul "esconde" muits processoes complexos
# facilitando o manuseio com os dados

#* obs: SQL funciona mto bem qunado a data esta bem formatinha e bem estruturada
#* caso contrario sera mais complexo trabalhar com ela. Por outro lado, podemos usar
#* python para embelezar os dados para o SQL

#* obs2: DBA = DataBase Administrator
#* Enquanto o Developer cuida da criação dos codigos e database, o DBA
#* cuida da manutenção do database funcionando


#! DATABASE MODEL

# Database model or database schema is the structure or format of a
# database, described in a formal language supported by the database
# management system

# 3 major database management system (DMS)

#? ORACLE: Large, commercial, eneterprise-scale, very tweakable (ajustavel)
#* Used in enterprise envirmoment
#? MySql: Simpler but very fast and scalable (open source)
#* used in webnetworking
#? SqlServer: Very nice (from Microsoft)
#* Another good option

# We'll be using SQLite (really small and good integration w/ python)

