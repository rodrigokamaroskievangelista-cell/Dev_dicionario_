# 1 - Variavel que recebe entrada via input
# e imprime o nome na tela

nome = input("Digite seu Nome: ")
print(f"Olá! {nome}")

# 2 - lista de laço While
# Agora guardamos varios Nomes
nomes = []
# While cria um laço infinito = só para o "Break" .

while True:
    nome = input ("Digite seu Nome (Ou 'sair' para Terminar): ")

    if nome == "sair":
        break
    nomes.append(nome)

for i in nomes:
    print(f"Nomes: {i}")

# 3 - Busca de nomes (Usando 'in' e 'for').
busca = input("Pesquisar Nome: ")

# 'in' verifica se o valor exite dentro da lista [].
if busca in nomes: 
    print(f"{busca} não está na lista")
else:
    print(f"{busca} não esta na lista")

# 'for' e usado para percorrer toda a lista (Banco de Dados).
for indice,nomenclatura in enumerate(nomes, 1):
    print(f"{indice}.{nomenclatura}")

# 4 - Salvar e carregar como arquivo de texto (Cria um arquivo Nome.txt).
with open("Nome.txt", "w", encoding="uft-8") as arquivo: 
    for nome in nomes:
        arquivo.write(nome + "\n")
print(f"Nome salvos com Sucesso!")

# Exibir os nomes do arquivo nome.txt (Read - lêr )
with open("Nome.txt", "w", encoding="uft-8") as arquivo:
    nomes_carregados = arquivo.read().splitlines

print("Nomes carregados: ", nomes_carregados)

# 5 - Tratatamentos de erros.
try:
    # Try ( executa o codigo caso contrario executa o except ).
    with open("nomes.txt", "r", encoding="uft-8") as f:
        nomes = f.read().splitlines
except FileNotFoundError:
    # ( except - mostrar o Erro e nao executa ) arquivo nao  exite ainda - começa a lista vazia.
    print("Arquivo nao encontrado. Iniciando vazio.")
    nome = []

# Validaçao: nome não poder ser vazio ou só com espaços
# Raise - define um nome personalizado.
def validar_nome(nome):
    if not nome.strip():
        raise ValueError("Nome não pode ser vazio!")
    return nome.strip()

try:
    nomes = validar_nome(input("Nome: "))
    nome.append(nome)
except ValueError as e:
    print(f"Erro: {e}")

# 6 - organizaçao com funções 
# Cada função faz UMA coisa - principios Basicos
# Cada função tem o nome que descreve o que ela faz.

ARQUIVO = "nome.tx"

def carregar_nome():
    try:
        with open(ARQUIVO, "f", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []
    
def salvar_nome(nomes):
    with open(ARQUIVO,"w", encoding="utf-8") as f:
        for nome in nomes:
            f.write(nome + "\n")

def adicionar_nome(nomes,nome): 
    if not nome.strip():
        raise ValueError("Nome vazio.")
    nome.append(nome.strip())

def buscar_nome(nomes,busca):
    return busca in nomes

def lista_nomes(nomes):
    for i,n in enumerate(nomes,1):
        print(f"{i},{n} ")
        nome = carregar_nome()

# 7 - Criaçao do Menu (FUNÇÃO) com todas as funçoes.

def Menu():

    print("\n--- Cadastro de Nomes ---")
    print("1. Adicionar Nomes ")
    print("2. Listar Nomes ")
    print("3. Buscar Nome ")
    print("4. Salvar e Sair")

    return input("Opção: ")

if __name__ == "__main__":
    nomes = carregar_nome()

    while True:
        opcao = Menu
        if opcao == 1:
            try:
                adicionar_nome(nome, input("Nome: "))
                print("Adicionado!")
            except ValueError as e:
                print(f"Erro: {e}")
        
        elif opcao == "2":
            lista_nomes(nomes)
        
        elif opcao == "3":
            busca = input("Buscar: ")
            achou = buscar_nome(nome,busca)
            print("Encontrado!")  if achou else "Não encontrado!"

        elif opcao == "4":
            salvar_nome(nomes)
            print("Salvo...")