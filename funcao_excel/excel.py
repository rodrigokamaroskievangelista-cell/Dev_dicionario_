def se(condicao, valor_verdadeiro, valor_falso):
    return valor_verdadeiro if condicao else valor_falso

alunos = [
    ("João", 40),
    ("Maria", 60),
    ("Pedro", 94),
    ("Ana", 60),
    ("Lucas", 70),
    ("Carla", 95),
    ("Mariana", 32),
    ("Fernanda", 86),
    ("Rodrigo", 85),
    ("Gustavo", 55),
    ("Beatriz", 34),
    ("Rafael", 25),
    ("Camila", 75),
    ("Bruno", 45),
    ("Larissa", 82),
    ("Felipe", 68),
    ("Sofia", 90),
    ("Diego", 58)
]
print(f"{'Aluno':<10} {'Nota':<5} {'Situação ':<10}")
print("-" * 36)

for nome,nota in alunos:
    situacao = se(nota >= 70, "Aprovado\t 🟢", se(nota >= 50, "Recuperação\t 🟡", "Reprovado\t 🔴"))
    print(f"{nome:<10} {nota:<5} {situacao:<10}")

print("-" * 36)


print("---- Status de Alunos ---- \n")

aprovados = 0
recuperacao = 0
reprovados = 0 

for nome,nota in alunos:
    if nota >= 70:
        aprovados += 1
    elif nota >= 50:
        recuperacao += 1
    else:
        reprovados += 1

print(f"Total de alunos: {len(alunos)}")
print(f"Alunos aprovados: {aprovados}")
print(f"Alunos em recuperação: {recuperacao}")
print(f"Alunos reprovados: {reprovados}")