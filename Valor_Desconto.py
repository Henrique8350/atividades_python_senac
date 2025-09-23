# Chamada de Importação
from typing import Final
# Fim da Chamada

# Definir Valores
VALOR_MINIMO_DESCONTO: Final = 100
DESCONTO: Final = 0.1 # Desconto de 10%

# Digite o Valor da Compra
valor_compra = int(input("digite o valor da sua compra: "))
# Fim da Digitação
calcular_desconto = valor_compra * DESCONTO
Valor_Final = valor_compra - calcular_desconto # Calculando Desconto

# Estrutura Condicional E Amostra no Terminal
if valor_compra >= VALOR_MINIMO_DESCONTO:
    print("Você recebeu um desconto de 10%!,o valor a pagar com desconto será: ",Valor_Final)
else:
    print("Compra abaixo do valor mínimo para desconto.")
# Fim da Estrutura Condicional E Amostra no Terminal
