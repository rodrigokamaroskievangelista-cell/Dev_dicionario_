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
    ("Rafael", 65),
    ("Camila", 75),
    ("Bruno", 45),
    ("Larissa", 82),
    ("Felipe", 68),
    ("Sofia", 90),
    ("Diego", 58)
]
print(f"{'Aluno':<10} {'Nota':<5} {'Situação':<10}")
print("-" * 30)

for nome,nota in alunos:
    situacao = se(nota >= 60, "Aprovado", "Reprovado")
    print(f"{nome:<10} {nota:<5} {situacao:<10}")

