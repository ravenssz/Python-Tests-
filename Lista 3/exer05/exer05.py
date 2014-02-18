class Usuario:
    def __init__(self, codigo, nome, peso, altura, gordura_corporal, nivel_atividade_fisica, calorias_a_consumir, sexo, valor_metabolico, massa_magra, peso_gordura, peso_gordura_ideal, peso_ideal, peso_a_perder, idade, listadeusuariotreino=[], listaderefeicao=[]):
        self.codigo = codigo
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.gordura_corporal = gordura_corporal
        self.nivel_atividade_fisica = nivel_atividade_fisica
        self.calorias_a_consumir = calorias_a_consumir
        self.sexo = sexo
        self.valor_metabolico = valor_metabolico
        self.massa_magra = massa_magra
        self.peso_gordura = peso_gordura
        self.peso_gordura_ideal = peso_gordura_ideal
        self.peso_ideal = peso_ideal
        self.peso_a_perder = peso_a_perder
        self.idade = idade
        self.listadeusuariotreino = listadeusuariotreino
        self.listaderefeicao = listaderefeicao
    def inserirRefeicao(self, refeicao):
        self.listaderefeicao.append(refeicao)
        
    def verificarRefeicao(self, refeicao):
        return refeicao in self.listaderefeicao

    def inserirUsuarioTreino(self, usuariotreino):
        self.listadeusuariotreino.append(usuariotreino)
        
    def verificarUsuarioTreino(self, usuariotreino):
        return usuariotreino in self.listadeusuariotreino

class Alimentos:
    def __init__(self, codigo, nome, categoria, quantidade, calorias, proteinas, carboidratos, gorduras, listaderefeicao=[]):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.calorias = calorias
        self.proteinas = proteinas
        self.carboidratos = carboidratos
        self.gorduras = gorduras        
        self.listaderefeicao = listaderefeicao

    def inserirRefeicao(self, refeicao):
        self.listaderefeicao.append(refeicao)
        
    def verificarRefeicao(self, refeicao):
        return refeicao in self.listaderefeicao
       
class Refeicao:
    def __init__(self, codigo, nome, total_calorias, horario, usuario, alimentos):
        self.codigo = codigo
        self.nome = nome
        self.total_calorias = total_calorias
        self.horario = horario 
        self.usuario = usuario
        self.alimentos = alimentos

class Historico:
    def __init__(self, codigo, peso_atual, peso_perdido, situacao, saldo_calorias, usuario):
        self.codigo = codigo
        self.peso_atual = peso_atual
        self.peso_perdido = peso_perdido
        self.situacao = situacao
        self.saldo_calorias = saldo_calorias
        self.usuario = usuario

class Treino:
    def __init__(self, codigo, nome, total_calorias_gastas, tempo_total, horario, data, listadeusuariotreino=[], listatreinoexercicio=[]):
        self.codigo = codigo
        self.nome = nome
        self.total_calorias_gastas = total_calorias_gastas
        self.tempo_total = tempo_total
        self.horario = horario
        self.data = data
        self.listadeusuariotreino = listadeusuariotreino
        self.listatreinoexercicio = listatreinoexercicio

    def inserirUsuarioTreino(self, usuariotreino):
        self.listadeusuariotreino.append(usuariotreino)
        
    def verificarUsuarioTreino(self, usuariotreino):
        return usuariotreino in self.listadeusuariotreino
    
    def inserirTreinoExercicios(self, treinoexercicios):
        self.listatreinoexercicio.append(treinoexercicios)
        
    def verificarTreinoExecicios(self, treinoexercicios):
        return treinoexercicios in self.listatreinoexercicio

class UsuarioTreino:
    def __init__(self, codigo, usuario, treino):
        self.codigo = codigo
        self.usuario = usuario      
        self.treino = treino

class Exercicios:
    def __init__(self, codigo, nome, calorias_gastas, numero_series, tempo_descanso, tempo_exercicio, lista_treinoexercicios=[]):
        self.codigo = codigo
        self.nome = nome
        self.calorias_gastas = calorias_gastas
        self.numero_series = numero_series
        self.tempo_descanso = tempo_descanso
        self.tempo_exercicio = tempo_exercicio
        self.lista_treinoexercicios = lista_treinoexercicios
    def inserirTreinoExercicios(self, treinoexercicios):
        self.lista_treinoexercicios.append(treinoexercicios)
        
    def verificarTreinoExecicios(self, treinoexercicios):
        return treinoexercicios in self.lista_treinoexercicios

class TreinoExercicios:
    def __init__(self, codigo, exercicios, treino):         
        self.codigo = codigo
        self.exercicios = exercicios
        self.treino = treino
        
    
        

