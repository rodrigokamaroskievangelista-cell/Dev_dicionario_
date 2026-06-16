# =====================================================
# 1 - VARIÁVEL QUE RECEBE ENTRADA VIA INPUT
#     E IMPRIME O NOME NA TELA
# =====================================================

nome = input("Digite seu Nome: ")
print(f"Olá! {nome}")


# =====================================================
# 2 - LISTA E LAÇO WHILE
#     AGORA GUARDAMOS VÁRIOS NOMES
# =====================================================

nomes = []

# While cria um laço infinito = só para com o "break".
while True:
    nome = input("Digite seu Nome (Ou 'sair' para Terminar): ")

    if nome == "sair":
        break

    nomes.append(nome)

for i in nomes:
    print(f"Nomes: {i}")


# =====================================================
# 3 - BUSCA DE NOMES (USANDO 'in' E 'for')
# =====================================================

busca = input("Pesquisar Nome: ")

# 'in' verifica se o valor existe dentro da lista [].
if busca in nomes:
    print(f"{busca} não está na lista")
else:
    print(f"{busca} não esta na lista")

# 'for' é usado para percorrer toda a lista (Banco de Dados).
for indice, nomenclatura in enumerate(nomes, 1):
    print(f"{indice}.{nomenclatura}")


# =====================================================
# 4 - SALVAR E CARREGAR COMO ARQUIVO DE TEXTO
#     (CRIA UM ARQUIVO Nome.txt)
# =====================================================

with open("Nome.txt", "w", encoding="uft-8") as arquivo:
    for nome in nomes:
        arquivo.write(nome + "\n")

print(f"Nome salvos com Sucesso!")

# Exibir os nomes do arquivo Nome.txt (Read = ler)
with open("Nome.txt", "w", encoding="uft-8") as arquivo:
    nomes_carregados = arquivo.read().splitlines

print("Nomes carregados: ", nomes_carregados)


# =====================================================
# 5 - TRATAMENTO DE ERROS
# =====================================================

try:
    # Try executa o código.
    # Caso ocorra erro, executa o except.
    with open("nomes.txt", "r", encoding="uft-8") as f:
        nomes = f.read().splitlines

except FileNotFoundError:
    # Arquivo não existe ainda.
    # Começa com a lista vazia.
    print("Arquivo nao encontrado. Iniciando vazio.")
    nome = []

# Validação:
# Nome não pode ser vazio ou conter apenas espaços.

# Raise define um erro personalizado.
def validar_nome(nome):
    if not nome.strip():
        raise ValueError("Nome não pode ser vazio!")
    return nome.strip()

try:
    nomes = validar_nome(input("Nome: "))
    nome.append(nome)

except ValueError as e:
    print(f"Erro: {e}")


# =====================================================
# 6 - ORGANIZAÇÃO COM FUNÇÕES
# =====================================================

# Cada função faz UMA coisa.
# Princípio básico de organização.
# O nome da função deve descrever o que ela faz.

ARQUIVO = "nome.tx"

def carregar_nome():
    try:
        with open(ARQUIVO, "f", encoding="utf-8") as f:
            return f.read().splitlines()

    except FileNotFoundError:
        return []

def salvar_nome(nomes):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for nome in nomes:
            f.write(nome + "\n")

def adicionar_nome(nomes, nome):
    if not nome.strip():
        raise ValueError("Nome vazio.")

    nome.append(nome.strip())

def buscar_nome(nomes, busca):
    return busca in nomes

def lista_nomes(nomes):
    for i, n in enumerate(nomes, 1):
        print(f"{i},{n} ")
        nome = carregar_nome()


# =====================================================
# 7 - CRIAÇÃO DO MENU (FUNÇÃO)
# =====================================================

def Menu():

    print("\n--- Cadastro de Nomes ---")
    print("1. Adicionar Nomes")
    print("2. Listar Nomes")
    print("3. Buscar Nome")
    print("4. Salvar e Sair")

    return input("Opção: ")


# =====================================================
# 8 - PROGRAMA PRINCIPAL
# =====================================================

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
            achou = buscar_nome(nome, busca)
            print("Encontrado!") if achou else "Não encontrado!"

        elif opcao == "4":
            salvar_nome(nomes)
            print("Salvo...")