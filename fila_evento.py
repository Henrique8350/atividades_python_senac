print("Sistema de Organização de Filas")
print("\n")
print("Seja Bem Vindo ao nosso evento,por favor siga para a área de verificação")
print("\n")

list_pessoas = ["Jorge","José","Maria","Pedro","Simone","Clara","Jefferson","Ana","Carol","Thiago"]

ingressos_validos = {
	"029": [0],
	"124": [1],
	"350": [2],
	"428": [3],
    "080": [4],
    "527": [5],
	"115": [6],
	"319": [7],
	"228": [8],
    "485": [9]
}

ingressos_ocupados = ["050","130","383","455","029","512","126","394","273","452"]

num_ingresso = (input("Digite o número do seu ingresso: "))

for i in list_pessoas:
    ingresso_valido = ingressos_validos
    ingresso_ocupado = ingressos_ocupados
    
    if num_ingresso in ingresso_valido:
        print("Ingresso válido")
    elif num_ingresso in ingresso_ocupado:
        print("Ingresso ocupado por outra pessoa")
    else:
        print("Ingresso não válido")
    break