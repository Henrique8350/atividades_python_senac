Umidade = "Possibilidade de Chuva,por precaucão,leve um guarda-chuva"
Limpido = "Sem Possibilidade de Chuva,o dia vai ser de sol e sem muitas nuvens,aproveite o dia"
Nebuloso = "Alerta de Tempestade se aproximando,para sua segurança,não saia de casa"

Climas = ["úmido","limpo","fechado"]

while True:
    Tempo = input("Como está o Tempo hoje? ( úmido,limpo ou fechado ) : ")
    Tempo_escolhido = Tempo
    if Tempo_escolhido == Climas[0]:
      print(Umidade)
      break
    elif Tempo_escolhido == Climas[1]:
      print(Limpido)
      break
    elif Tempo_escolhido == Climas[2]:
      print(Nebuloso)
      break
    else:
    	print("Digite um clima existente")
