import random

class Cartas:
    def __init__(self,nome,naipe):
        self.nome = nome
        self.naipe = naipe

class Baralho:
    def __init__(self,cartas=[]):
        self.cartas = cartas
        listadecartas = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        listadenaipes = ["E","O","P","C"]
        for y in xrange(len(listadenaipes)):
            for x in xrange(len(listadecartas)):
                carta = Cartas(listadecartas[x],listadenaipes[y])    
                self.cartas.append(carta)
                
    def comprarCarta(self):
        if not len(self.cartas) == 0:
            return self.cartas.pop()
        return None
        
    def verificarCarta(self):
        if not len(self.cartas) == 0:
            return True
        return False
        
    def imprimirBaralho(self):
        baralho = ''
        for k in xrange(len(self.cartas)):
            baralho += ('carta: %s - naipe: %s'%(self.cartas[k].nome,self.cartas[k].naipe))
        return baralho
        
    def embaralharBaralho(self):
        random.shuffle(self.cartas)
        
    def sortearJogo(self):
        inicio = []
        for x in xrange(11):
            inicio.append(self.comprarCarta())
        return inicio

class Jogador:
    def __init__(self,cartasdojogador=[]):
        self.cartasdojogador = cartasdojogador
        
    def printCartasDoJogador(self):
        cartas = ''
        for k in xrange(len(self.cartasdojogador)):
            cartas += ('carta: %s - naipe: %s'%(self.cartasdojogador[k].nome,self.cartasdojogador[k].naipe))
        return cartas
        
class Jogo:
    def __init__(self,baralho,jogadores=[]):
        self.baralho = baralho
        self.jogadores = jogadores
        
    def iniciarJogador(self):
        jogador = Jogador(baralho.sortear_jogo())
        self.jogadores.append(jogador)
