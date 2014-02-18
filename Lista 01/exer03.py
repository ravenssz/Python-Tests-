#coding: utf-8

#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um
#fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante
#perderá. Exiba o total de dias.
def calcular_tempo_de_vida(cigarros_fumados, anos_fumados):
	cigarros_dia = (cigarros_fumados * (anos_fumados * 365))
	contador_minuto = 0
	dia = 0
	for z in range(cigarros_dia):
		contador_minuto+=1
		if contador_minuto == 144:
			dia+=1
			contador_minuto = 0
	return dia


	

cigarros_fumados = input("Digite a quantidade de cigarros fumados em um dia: ")
anos_fumados = input("Digite o total de anos em que fumou: ")
print "O total de dias perdidos com o cigarro foi: %.2f"%(calcular_tempo_de_vida(cigarros_fumados, anos_fumados))
