# Nosso "Banco de Dados" de Usuarios

# 1 exercicio: Criar um Dicionário para armazenar os dados dos usuários
print("1 ----- Atividade -----")
print("\n")

usuarios = [
["Alice", "alice@gmail.com", 30], # 0
["Bob", "bob@gmail.com", 25], # 1
["Charlie", "charlie@gmail.com", 35], #2
["Eve", "eve@gmail.com", 28], # 3
["David", "david@gmail.com", 40] # 4
]

for usuario in range(len(usuarios)):
    nome = usuarios[usuario][0]
    email = usuarios[usuario][1]
    idade = usuarios[usuario][2]
    print(f"Nome: {nome} | Email: {email} | Idade: {idade}")

print("-" * 50)

###########################################################################################

#2 use uma variavel para armazenar o primeiro usuario eo print para exibir este usuario
print("2 ----- Atividade -----")
print("\n")

print(f"Nomes: {usuarios[0][0]} | Email: {usuarios[0][1]} | Idade: {usuarios[0][2]}")
emails = [usuario[1] for usuario in usuarios]
idades = [usuario[2] for usuario in usuarios]

print("-"*50)

# 3 Acesse  e  exiba o nome do segundo usuario definido na lista somente "Nome". Crie uma variavel.
print("3 ----- Atividade -----")
print("\n")

print(f"Nomes: {usuarios[1][0]} | Email: {usuarios[1][1]} | Idade: {usuarios[1][2]}")
emails = [usuario[1] for usuario in usuarios]
idades = [usuario[2] for usuario in usuarios]