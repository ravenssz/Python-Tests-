#coding: utf-8

#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o
#preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

def calcular_kilometro(kilometros, dias):
	return kilometros * 0.15 + dias * 60


kilometros = input("Digite a quantidade de Kilometros percorridos: ")
dias = input("Digite a quantidade de dias no qual o carro ficou alugado: ")

print "O total a ser pago é:",(calcular_kilometro(kilometros, dias))

print ("O total a ser pago é: %.2f, %i dias, %i km"%(calcular_kilometro(kilometros, dias),dias,kilometros))
