#coding: utf-8

#Dizemos que um número natural é triangular se ele é produto de três números naturais
#consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro
#não-negativo n, verificar se n é triangular


def verificar_triangular(numero):		
	for x in range(numero):
		if x * (x + 1) * (x + 2) == numero:
		   return 1
	return 0


numero = input("Digite um numero: ")
if verificar_triangular(numero) == 1:
	print "%i é triangular "%numero
else:
	print "%i não é triangular "%numero

