def estoque(produto):
    if produto == "abobora":
        return 5
    elif produto == "melancia":
        return 2
    elif produto == "banana":
        return 6
    elif produto == "manga":
        return 7
    elif produto == "mandioca":
        return 1
    else:
        return "Produto não encontrado"

print("=== Estoque atual ===")
produtos = ["abobora", "melancia", "banana", "manga", "mandioca"]

i = 0
while i < len(produtos):
    print(produtos[i])
    i += 1

produto = input("\nDigite o nome do produto: ").lower()
quantidade = estoque(produto)

if quantidade == "Produto não encontrado":
    print(quantidade)
else:
    print(f"Há {quantidade} unidades de {produto} em estoque.")