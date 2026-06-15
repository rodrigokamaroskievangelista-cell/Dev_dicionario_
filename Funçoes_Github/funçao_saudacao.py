def saudacao(nome, mensagem = "Seja Bem-Vindo!"):
    print(f"Olá {nome}, {mensagem}")

saudacao("Ana")
saudacao("Bob","Bom-Dia!")

def cadastro_user(nome,idade,admin = False):
    print(f"Nome: {nome} | idade:  {idade} | Admin: {admin}  ")

cadastro_user(idade = 30, nome = "Rodrigo")
cadastro_user("James",25, admin = True)

# Nome: Rodrigo | idade:  30 | Admin: False  
# Nome: James | idade:  25 | Admin: True  