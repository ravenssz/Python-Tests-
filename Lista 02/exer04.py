#coding: utf-8
import math 
#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma
#ax2+ bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
#informando ao usuário nas seguintes situações:
#1. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e
#o programa não deve fazer pedir os demais valores, sendo encerrado;
#2. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao
#usuário e encerre o programa;
#3. Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
#informe-a ao usuário;
#4. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;






a = input("Digite o valor de a: ")
if a == 0:
	print "valor inválido!" 
else:	
	b = input("Digite o valor de b: ")
	c = input("Digite o valor de c: ")
	delta = (b^2+(-4*a*c))
	if delta < 0:
		print "Não possui valores reais no delta"
		print delta
		print b
	else:
		r1 = float((-(b)+(math.sqrt(delta)))/(2*a))
		r2 = float((-(b)-(math.sqrt(delta)))/(2*a))
		print delta
		print b
		print "Resolvendo %dx^2+(%dx)+(%d) - Resultado X1: %.1f " % (a,b,c,r1)
		print "Resolvendo %dx^2+(%dx)+(%d) - Resultado X2: %.1f " % (a,b,c,r2)
