#coding: utf-8

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que
#são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça
#um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e
#o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
#descontos e o salário líquido, conforme a tabela abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$


def calcular_salario_liquido(bruto):
	renda = bruto * 0.11
	liquido = bruto - renda
	inss = bruto * 0.08
	liquido -= inss
	sindicato = bruto * 0.05
	liquido -= sindicato
	print "Descontos \n"
	print "Imposto de renda: %f"%renda
	print "INSS: %f"%inss
	print "Sindicato: %f"%sindicato
	print "Total Liquido %f"%liquido
	


salariohora = input("Digite o valor de seu salário/hora: " )
horatrabalhada = input("\nDigite o total de hora trabalhada: ")
bruto = salariohora * horatrabalhada
print "Seu salário bruto é: %i"%bruto
calcular_salario_liquido(bruto)

