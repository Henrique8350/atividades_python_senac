import random

def criar_contaBanco():
    while True:
        conta_num = random.randint(10000000, 99999999)
        nome = str(input("\nInsira o seu nome completo: "))
        senha_op = int(input("\nInsira uma senha de quatro dígitos numéricos para realizar operações: "))
        saldo = float(input("\nVocê deseja já realizar uma depósito?\nSe sim, digite o valor do seu saldo, caso não digite 0: "))
        historico_tr = []

        if nome.isalpha():
            print(f"\nConta criada com sucesso:\nNúmero da conta: {conta_num}\nNome: {nome}")
            print(f"Senha de operações: {senha_op}\nSaldo: {saldo}\nHistório{historico_tr}")
            break
        else:
            print("\nO nome deve ser digitado somente com letras.")
            print("\nRecomece o processo de criação de conta.")

criar_contaBanco()