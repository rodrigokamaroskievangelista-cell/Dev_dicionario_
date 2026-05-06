# Criando um Dicionario

produto = {"nome": "Teclado", "preco": 150, "em_estoque": True}

# Acessando um valor
print(produto["nome"])

# Modificaçao um valor
produto["preco"] = 135.00

# Adicionar um novo par
produto["Quantidade"] = 15
produto["Divergência"] = 2

# Lista Atualizado
print(produto) 
# {'nome': 'Teclado', 'preco': 135.0, 'em_estoque': True, 'Quantidade': 15, 'Divergência': 2}