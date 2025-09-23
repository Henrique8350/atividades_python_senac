# Chamada de Importação
from typing import Final
# Fim da Chamada

# Definir Idades
IDADE_MINIMA: Final = 18
IDADE_MAX_VOTO: Final = 70
# Fim da Definição

# Digite sua Idade
idade = int(input("digite sua idade: "))
# Fim da Digitação

# Mostrar no Terminal
if idade >= IDADE_MINIMA:
    print("Você já é maior de idade!")
elif idade >= IDADE_MAX_VOTO:
    print("Você já está com idade acima do permitido para voto,o voto não é mais necessário")
else:
    print("Você ainda é menor de idade.")
# Fim da Amostra