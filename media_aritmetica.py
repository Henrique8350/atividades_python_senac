# Digite 3 números
num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
num3 = int(input("digite o terceiro número: "))
# Fim da Digitação

# Condição maior/menor

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

# Fim das Condições

# Definição da Média

media = ( num1 + num2 + num3 ) / 3

# Fim da definição

# Mostrar no Terminal
print("\n resultado: ")
print("\n O número maior é: ",maior)
print("\n O número menor é: ",menor)
print("\n A média aritmética é: ",media)
# Fim da Amostra
