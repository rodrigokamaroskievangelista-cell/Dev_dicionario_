#fucionarios = [{
# "setor": "juridico","Nome": "Anderson", "Salario": 1450.00, "Cargo": "Gerente", "Bônus":
# }]

def cadastrar_funcionario():
    print("="*50)
    print("Cadastrar funcionario")
    print("="*50)

    nome = input("Nome do Usuario: ")
    setor = str(input("Setor (jurídico/Marketing/TI/Vendas)"))
    salario = float (input("Salário (Ex: 1450.00): R$"))
    cargo = str (input("Cargo (Gerente/Analista): "))
    bonus = float (input("Bônus (Ex: 850.00): R$"))

    linha = f"{setor} | {nome} | {salario:.2f} | {cargo} | {bonus:.2f}\n"

    with open("funcionarios.txt","a", encoding="utf-8") as arquivo: arquivo.write(linha)

    print("\n Funcionarios cadastrado com sucesso!")
    print(f"Dados salvos em 'funcionarios.txt")
    return {"Setor": setor, "Nome": nome, "salario": salario, "Cargo": cargo, "Bônus": bonus}

novo_funcionario = cadastrar_funcionario()
print("\nDados cadastrado: ", novo_funcionario)