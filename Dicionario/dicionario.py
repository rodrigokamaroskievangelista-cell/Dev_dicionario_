# **kwargs - argumentos variaveis 
# Captura qualquer quantidade de argumentos como dicionario.



def exibir_info(**dados):
    for chave, valor in  dados.items():
        print(f"{chave}: {valor}")

exibir_info(Nome="Calor", idade=30, cidade="SP", partido="Bolsonaro")