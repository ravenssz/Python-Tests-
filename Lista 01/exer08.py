#coding: utf-8

#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se
#os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo
#é: equilátero, isósceles ou escaleno
#1)Equilátero = um triângulo que possui seus 3 lados congruentes.

#2)Isósceles = um triângulo que possui 2 de seus lados iguais.

#3)Escaleno = um triângulo que não possui lados iguais entre si. ..

def verificar_triangulo(trium, tridois, tritres):
	if trium == tridois and tridois == tritres:
		return "Equilátero"
	elif trium != tridois and tridois != tritres:
		return "Escaleno" 
	else:
		return "Isósceles"

trium = input("Digite o primeiro lado do triangulo: ")
tridois = input("\nDigite o segundo lado do triangulo: ")
tritres = input("\nDigite o terceiro lado do triangulo: ")


if trium+tridois > tritres and trium + tritres > tridois and tridois + tritres > trium:
	if trium - tridois < tritres and trium - tritres < tridois and tridois - tritres < trium:
		print "O triangulo é: %s"%verificar_triangulo(trium, tridois, tritres)
else:
	print "INVÁLIDO"

