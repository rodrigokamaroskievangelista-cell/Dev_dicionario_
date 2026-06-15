# Funçoes com "args- calculadora Flexivel "

def estatistica(*numeros):
    total = sum(numeros)
    media = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    
    print(F"Total: {total} | Media: {media:.2f} | Max: {maximo} | Min: {minimo}")

#tupla: 

estatistica(10,20,30)
estatistica(50,68,80,90,46)
estatistica(70,89,49)

#Lista 

lista = (80,90,95)
estatistica(*lista)