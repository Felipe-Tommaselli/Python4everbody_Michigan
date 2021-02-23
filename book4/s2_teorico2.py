# Using SQLite

#* Abrir o SQLite, clicar em criar novo banco de dados
#* colocar um nome qlqr

#! Criar tabela 

# Ir para Executar SQL:
# codigo pra por dentro:
#? CREATE TABLE Users(
#?      name VARCHAR(128),
#?      email VARCHAR(128)
#? )  

# cria uma tabela chamada Users com um espaco de nome e de email 
# os quais sao uma variavel que cabem 128 caracteres
# por algum motivo desconhecido não pode por num feio de carac
# se quiser por bastante carac tem q por 1024

#! Adicionar elementos (rows/ linhas)

# ir em Navegar dados e em "Inserir um novo registro da tabela atual"
# (do lado do icone da impressora)

# Ou usando o SQL Insert

# No executar SQL, apagar oq ja tem e adiconar
#? INSERT INTO Users(name, email) VALUES ('brendha', 'brendhaariadne@hotmail.com')

#! Deletando elementos (rows/ linhas)

# No executar SQL, apagar oq ja tem e adiconar
#? DELETE * FROM Users WHERE email = 'brendhaariadne@hotmail.com'

#! Atualizando um campo com restrição (não aplicar ao banco inteiro)

# No executar SQL, apagar oq ja tem e adiconar
#? UPDATE Users SET name = 'Juquinha' WHERE email = 'beatriztommaselli@gmail.com'


#* Retrieving Records

#! SELECT

#? SELECT * FROM Users
# Retorna a tabela toda

#? SELECT * FROM Users WHERE email = Felipetommaselli@gmail.com'
# Retorna a linha com o email pedido

#! Sorting

#? SELECT * FROM Users ORDER BY email
# Ordena por ordem alfabetica dos emails