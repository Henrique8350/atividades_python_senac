import random

def criar_usuario():
    login_nome = str(input("\nCrie um nome para o seu login: "))
    senha = str(input("\nCrie uma senha de seis dígitos: "))
    codigo_ver = random.randint(1000, 9999)

    cadastros = [login_nome] and {
        'senha': senha,
        'codigo_ver': codigo_ver
    }

    print(f"\nUsuário cadastrado:\nLogin: {login_nome}\nSenha: {senha}\nCódigo de verificação: {codigo_ver}\n")
    print(cadastros)
criar_usuario()

