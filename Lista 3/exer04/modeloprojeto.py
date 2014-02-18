class AvaliadorProjeto:
    def __init__(self, datacomeco, dataentrega, parecer, nota, avaliador, projeto):
        self.datacomeco = datacomeco
        self.dataentrega = dataentrega
        self.parecer = parecer
        self.nota = nota
        self.avaliador = avaliador
        self.projeto = projeto




class IntegranteProjeto:
    def __init__(self,datainicio, datafim, cargo, setor, projeto, integrante):

        self.datainicio = datainicio
        self.datafim = datafim
        self.cargo = cargo
        self.setor = setor
        self.projeto = projeto
        self.integrante = integrante

class Bolsista:
    def __init__(self, codigo, nome, matricula, cpf, curso, periodo, datadenascimento, endereco, bolsistaprojeto=[]):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.curso = curso
        self.periodo = periodo
        self.datadenascimento = datadenascimento 
        self.endereco = endereco
        self.bolsistaprojeto = bolsistaprojeto
    
class BolsistaProjeto:

    def __init__(self, datainicio, datafim, cargo, setor, bolsista, projeto):
        self.datainicio = datainicio   
        self.datafim = datafim
        self.cargo = cargo
        self.setor = setor
        self.bolsista = bolsista
        self.projeto = projeto


        
