print("AGENCIA DE VIAGENS")

valor_dispo = int(input("Digite o valor total disponível para a viagem (R$): "))

loc_orig = str(input("Digite a sua cidade de origem: "))

Destino = ["Recife/PE","São Paulo/SP","Rio de Janeiro/RJ","Bahia/BA","Belo Horizonte/BH"]

for i in (Destino):
    print("Opções de Destino Disponíveis: ")
    primeiro_Destino = Destino[0]
    print(f"1: {primeiro_Destino}")
    segundo_Destino = Destino[1]
    print(f"2: {segundo_Destino}")
    terceiro_Destino = Destino[2]
    print(f"3: {terceiro_Destino}")
    quarto_Destino = Destino[3]
    print(f"4: {quarto_Destino}")
    quinto_Destino = Destino[4]
    print(f"5: {quinto_Destino}")
    break

escolha_dest = int(input(f"Escolha o Destino {0,1,2,3,4}: "))
"""
print("1 - cadastro\n2 - consultar")
"""
valor_onibus = 200
valor_Van = 100
valor_Aviao = 400

opc_transporte = [f"Ônibus (R${valor_onibus})",f"Van (R$ {valor_Van})",f"Avião (R$ {valor_Aviao})"]


for a in (opc_transporte):
    print("\n")
    print("Opções de Transporte Disponíveis: ")
    primeiro_Transporte = opc_transporte[0]
    print(f"1: {primeiro_Transporte}")
    segundo_Transporte = opc_transporte[1]
    print(f"2: {segundo_Transporte}")
    terceiro_Transporte = opc_transporte[2]
    print(f"3: {terceiro_Transporte}")
    break

escolha_transpo = int(input(f"Escolha o Transporte {0,1,2}: "))


"""
for i in (Destino):
    print("Opções de Destino Disponíveis: ")
    primeiro_Destino = Destino[0]
    print(f"1: {primeiro_Destino}")
    segundo_Destino = Destino[1]
    print(f"2: {segundo_Destino}")
    terceiro_Destino = Destino[2]
    print(f"3: {terceiro_Destino}")
    quarto_Destino = Destino[3]
    print(f"4: {quarto_Destino}")
    quinto_Destino = Destino[4]
    print(f"5: {quinto_Destino}")
    break

"""
    
    