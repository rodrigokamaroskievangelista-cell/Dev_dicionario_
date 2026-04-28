def exibir_info(**dados):
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')

# Criar um Dicionario Vazio para armazenar as entradas

info_usuario =  {}

print("Digite as informaçoes (ou 'sair' na chave para encerrar)")

while True:
    chave = input("Nome do campo (ex: Profissão): ")
    if chave.lower == 'sair':
        break
    valor = input(f"Salario {chave}: ")
    info_usuario[chave] = valor

# Usando ** para desempacotar o dicionario como argumento

exibir_info(**info_usuario)