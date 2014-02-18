#coding: utf-8

#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por
#exemplo, o programa deve converter 14:25 em 2:25. A entrada é dada em dois inteiros.
#Fazer uma função para a conversão do valor. Inclua um loop que permita que o usuário
#repita esse cálculo para novos valores de entrada todas as vezes que desejar.


def converter_hora(hora):
	if hora > 12 and hora != 24:
		contador = 0
		for x in range(hora):
			if x >= 12:
				contador+=1
		return contador
	elif hora == 24:
		return 0
	else:
		return hora
controle = 1
while controle != 0:
	hora = input("Digite a hora a ser convertida: ")
	minuto = input("Digite o minuto: ")
	print "Convertido: %i:%i"%(converter_hora(hora),minuto)
	controle = input("Continuar? 1(sim)/0(nao): ")
print("Obrigado até mais")
