print("AGENCIA DE VIAGENS")

while True:
	try:
		valor_dispo = int(input("Digite o valor total disponível para a viagem (R$): "))
		break
	except ValueError:
		print("Entrada inválida. Por favor, digite um número.")

print("\n")

while True:
    loc_orig = input("Digite a sua cidade de origem: ")
    # Verifica se a string contém apenas letras,espaços ou hífens
    if all(char.isalpha() or char.isspace() or char == '-' for char in loc_orig):
        break  # Se a entrada for válida, sai do loop
    else:
        print("Entrada inválida. Por favor, digite apenas o nome da cidade,sem números ou caracteres especiais ( exceto hífen ).")

Destino = ["Recife/PE","São Paulo/SP","Rio de Janeiro/RJ","Bahia/BA","Belo Horizonte/BH"]

for i in (Destino):
    print("\n")
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

escolha_dest = input(f"Escolha o Destino {0,1,2,3,4}: ")
"""
print("1 - cadastro\n2 - consultar")
"""
escolha_valida = [ '0' , '1' , '2' , '3' , '4' ]
	
while escolha_dest not in escolha_valida:
	try:
		escolha_dest = (input(f"Escolha o Destino {escolha_valida}: "))
		if escolha_dest not in escolha_valida:
			print("Escolha um número válido (0 a 4). Por favor, tente novamente.")
	except ValueError:
		print("Entrada inválida. Por favor, digite um número válido.")

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
    


escolha_transpo = input(f"Escolha o Transporte {0,1,2}: ")

escolha_valida_transpo =  [ '0' , '1' , '2' ]
	
while escolha_transpo not in escolha_valida_transpo:
	try:
		escolha_transpo = (input(f"Escolha o Transporte {escolha_valida_transpo}: "))
		if escolha_transpo not in escolha_valida_transpo:
			print("Escolha um número válido (0 a 2). Por favor, tente novamente.")
	except ValueError:
		print("Entrada inválida. Por favor, digite um número válido.")

print("\n")

"""
for b in (Destino):
    print("\n")
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
    
    