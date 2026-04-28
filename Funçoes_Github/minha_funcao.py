# Geral = "Essa variavel pode chamar onde quiser"

# def minha_funcao():
#     print("Essa minha funçao")
#     local = "Essa variavel so pode ser utilizada na funçao"

#     #Chamar minha funçao
#     minha_funcao()

#     # print(local)
#     print(Geral)

nome = "Alan" # Global #Rua ou Publico

def saudacao():
    sobrenome = 'code' #Local
    print(f"Olá, {nome} {sobrenome}")
saudacao()

def somar(n1, n2):
    print(f"A soma: {n1 + n2}") # n1 e n2 sao o parâmetros
somar (6,40) # 6 e 40 sao os argumentos

def formatar_real(valor):
    return f"R$ {valor:.2f}".replace(",", "X").replace("." , ",").replace("X" , ".") 
#replace substituir ("," passa a ser ".")
#uso:
preco_hospedagem = 1250.90
print(formatar_real(preco_hospedagem)) # R$ 1250.90

## atualizado