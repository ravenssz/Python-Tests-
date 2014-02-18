#coding: utf-8
import random
#Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras
#lidas de um arquivo palavra e escolherá uma aleatoriamente. O jogador poderá errar 6
#vezes antes de ser enforcado.
#Digite uma letra: A
#-> Você errou pela 1a vez. Tente de novo!
#Digite uma letra: O
#A palavra é: _ _ _ _ O
#Digite uma letra: E
#A palavra é: _ E _ _ O
#Digite uma letra: S
#-> Você errou pela 2a vez. Tente de novo!


consulta = open("arquivo.txt")
palavra = consulta.readlines()
consulta.close()
	
print("Jogo da forca \n")
parametro = 1
while parametro == 1:
	x = random.randint(0,6)
	palavra_letra = palavra[x]
	verificador_errado = 0
	verificador_erros = 0
	lista_de_acertos = []
	lista = []
	letra_digitada=[]
	for x in range(len(palavra_letra)-1):
		lista.append('_ ')
		
	while verificador_errado < 6:
		verificador_certo = 0
		verificador_erros = 0
		print ""
		for x in range(len(palavra_letra)-1):
			print lista[x],
		print ""	
		letra = raw_input('\nDigite uma letra: ')
		letra_digitada.append(letra)
		for x in range(len(palavra_letra)-1):
			while (len(palavra_letra)-1):			
				if (letra == palavra_letra[x]):				
					if lista[x] == '_ ':					
						print '\nCerta resposta!!!'
						lista[x]= letra
						lista_de_acertos.append(letra)
						verificador_certo = 1
					else:
						print 'Essa letra ja foi digitava, favor escolher outra.'
						verificador_certo = 1
				break		
			if verificador_certo == 0:
				verificador_erros += 1	
		if verificador_erros ==len(palavra_letra)-1:
			verificador_errado += 1
			print " %i erro, tente novamente"%verificador_errado
			if verificador_errado == 6:
				print "Game over!"	
				print "\nA palavra certa era:",
				for x in range(len(palavra_letra)-1):
					print palavra_letra[x],
		print "\n"		
		for x in range(len(palavra_letra)-1):
			if len(lista_de_acertos)==len(palavra_letra)-1:
				print "You Win!"
				verificador_errado = 6
			break
		print "\nLetras que voce ja digitou:",
		for x in range(len(letra_digitada)):
			print letra_digitada[x],',',
	opcao= input ("\nJogar denovo [1] sair [0]")
	
