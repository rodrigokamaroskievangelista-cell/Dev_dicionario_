import random

simbolos = ["👒", "⚔️", "🧭", "🍖", "💰"]
saldo = 200.0

print("Bem Vindo ao Casino do Luffy")

while saldo >= 2:
    input("Pressione Enter para jogar (R$ 2.00 por rodada)...")
    saldo -= 2

    resultado = [random.choice(simbolos) for _ in range(3)]
    print("Resultado:", resultado)

    if resultado[0] == resultado[1] == resultado[2]:
        premio = 20
        saldo += premio
        print(f"Você ganhou R$ {premio}!")
    else:
        print("Que pena! Tente novamente.")

print(f"Saldo final: R$ {saldo}")
