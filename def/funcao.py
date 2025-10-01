def cadastrar_usuario():
    cadastro_usuario = ["João","Maria","Pedro","Jorge","Tânia"]
    usuario = input("Digite seu nome e o sistema vai verificar se você está cadastrado ou não : ").capitalize
    for i in cadastro_usuario:
        if usuario in cadastro_usuario:
            print("Você está cadastrado")
            break
        else:
            print("Você não está cadastrado")
            break
cadastrar_usuario()