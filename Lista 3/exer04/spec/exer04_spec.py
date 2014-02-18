import unittest
from should_dsl import should
from exer04 import *
from datetime import date

class AvaliadorSpec(unittest.TestCase):
    
    def it_creates_a_avaliador_object(self):
    
        avaliador = Avaliador(1, "nome", [])
        avaliador.codigo |should| equal_to(1)
        avaliador.nome |should| equal_to("nome")
        avaliador.listaavaliadorprojeto |should| equal_to([])

    def it_inserir_lista_avaliador_projeto(self):
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        avaliador = Avaliador(1, "nome", [])
        avaliadorprojeto = AvaliadorProjeto("01-01-01", "02-02-02", "parecer", 10, avaliador, projeto)
        avaliador.inserirAvaliadoProjeto(avaliadorprojeto)
        (avaliadorprojeto in avaliador.listaavaliadorprojeto) |should| equal_to(True)

    def it_verificar_lista_avaliador_projeto(self):
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        avaliador = Avaliador(1, "nome", [])
        avaliadorprojeto = AvaliadorProjeto("01-01-01", "02-02-02", "parecer", 10, avaliador, projeto)
        avaliador.inserirAvaliadoProjeto(avaliadorprojeto)
        avaliador.verificaAvaliadoProjeto(avaliadorprojeto) |should| equal_to(True)


class BolsistaSpec(unittest.TestCase):

    
    def it_creates_a_bolsista_object(self): 

        bolsista = Bolsista(1, "nome", "matricula", "cpf", "curso", "periodo","11/11/11", "endereco",[])
        bolsista.codigo |should| equal_to(1)
        bolsista.nome |should| equal_to("nome")
        bolsista.matricula |should| equal_to("matricula")
        bolsista.cpf |should| equal_to("cpf")
        bolsista.curso |should| equal_to("curso")
        bolsista.periodo |should| equal_to("periodo")
        bolsista.datadenascimento |should| equal_to("11/11/11")
        bolsista.endereco |should| equal_to("endereco")
        bolsista.listabolsistaprojeto |should| equal_to([])
        
    def it_verificar_lista_bolsista_projeto(self):
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        bolsista = Bolsista(1, "nome", "matricula", "cpf", "curso", "periodo","11/11/11", "endereco",[])
        bolsistaprojeto = BolsistaProjeto("01-01-01", "01-01-01", "cargo", "setor", bolsista, projeto)
        bolsista.inserirBolsistaProjeto(bolsistaprojeto)
        bolsista.verificaBolsistaProjeto(bolsistaprojeto) |should| equal_to(True)

    def it_inserir_lista_bolsista_projeto(self):
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        bolsista = Bolsista(1, "nome", "matricula", "cpf", "curso", "periodo","11/11/11", "endereco",[])
        bolsistaprojeto = BolsistaProjeto("01-01-01", "01-01-01", "cargo", "setor", bolsista, projeto)
        bolsista.inserirBolsistaProjeto(bolsistaprojeto)
        (bolsistaprojeto in bolsista.listabolsistaprojeto) |should| equal_to(True)

class IntegranteSpec(unittest.TestCase):

    def it_creates_a_integrante_object(self):
        integrante = Integrante(1, "nome", "cpf", 222222, "endereco", "email",[])
        integrante.codigo |should| equal_to(1)
        integrante.nome |should| equal_to("nome")
        integrante.cpf |should| equal_to("cpf")
        integrante.telefone |should| equal_to(222222)
        integrante.endereco |should| equal_to("endereco")
        integrante.email |should| equal_to("email")
        integrante.listaintegranteprojeto |should| equal_to([])

    def it_inserir_lista_integrante_projeto(self):
        integrante = Integrante(1, "nome", "cpf", 222222, "endereco", "email",[]) 
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])       
        integranteprojeto = IntegranteProjeto("01-01-01", "02-02-02", "cargo", "setor", projeto, integrante)
        integrante.inserirIntegranteProjeto(integranteprojeto)
        (integranteprojeto in integrante.listaintegranteprojeto) |should| equal_to(True)
    
    def it_verificar_lista_integrante_projeto(self):
        integrante = Integrante(1, "nome", "cpf", 222222, "endereco", "email",[]) 
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])       
        integranteprojeto = IntegranteProjeto("01-01-01", "02-02-02", "cargo", "setor", projeto, integrante)
        integrante.inserirIntegranteProjeto(integranteprojeto)
        integrante.verificarIntegranteProjeto(integranteprojeto) |should| equal_to(True)        

class ProjetoSpec(unittest.TestCase):

    def it_creates_a_projeto_object(self):
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        projeto.codigo |should| equal_to(1)
        projeto.titulo |should| equal_to("titulo")
        projeto.relatorio |should| equal_to("relatorio")
        projeto.datadesubmissao |should| equal_to("11-11-11")
        projeto.resumo |should| equal_to("resumo")
        projeto.situacao |should| equal_to("situacao")
        projeto.listadeavaliadorprojeto |should| equal_to([])
        projeto.listadebolsistaprojeto |should| equal_to([])
        projeto.listadeintegranteprojeto |should| equal_to([])
        projeto.listadepesquisador |should| equal_to([])

    def it_inserir_lista_avaliador_projeto(self):
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        avaliador = Avaliador(1, "nome", [])
        avaliadorprojeto = AvaliadorProjeto("01-01-01", "02-02-02", "parecer", 10, avaliador, projeto)
        projeto.inserirAvaliadoProjeto(avaliadorprojeto)
        (avaliadorprojeto in projeto.listadeavaliadorprojeto) |should| equal_to(True)

    def it_verificar_lista_avaliador_projeto(self):
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        avaliador = Avaliador(1, "nome", [])
        avaliadorprojeto = AvaliadorProjeto("01-01-01", "02-02-02", "parecer", 10, avaliador, projeto)
        projeto.inserirAvaliadoProjeto(avaliadorprojeto)
        projeto.verificaAvaliadoProjeto(avaliadorprojeto) |should| equal_to(True)

    def it_inserir_lista_integrante_projeto(self):
        integrante = Integrante(1, "nome", "cpf", 222222, "endereco", "email",[]) 
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])       
        integranteprojeto = IntegranteProjeto("01-01-01", "02-02-02", "cargo", "setor", projeto, integrante)
        projeto.inserirIntegranteProjeto(integranteprojeto)
        (integranteprojeto in projeto.listadeintegranteprojeto) |should| equal_to(True)

    def it_verificar_lista_integrante_projeto(self):
        integrante = Integrante(1, "nome", "cpf", 222222, "endereco", "email",[]) 
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])       
        integranteprojeto = IntegranteProjeto("01-01-01", "02-02-02", "cargo", "setor", projeto, integrante)
        projeto.inserirIntegranteProjeto(integranteprojeto)
        projeto.verificarIntegranteProjeto(integranteprojeto) |should| equal_to(True)

    def it_verificar_lista_bolsista_projeto(self):
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        bolsista = Bolsista(1, "nome", "matricula", "cpf", "curso", "periodo","11/11/11", "endereco",[])
        bolsistaprojeto = BolsistaProjeto("01-01-01", "01-01-01", "cargo", "setor", bolsista, projeto)
        projeto.inserirBolsistaProjeto(bolsistaprojeto)
        projeto.verificaBolsistasProjeto(bolsistaprojeto) |should| equal_to(True)

    def it_inserir_lista_bolsista_projeto(self):
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        bolsista = Bolsista(1, "nome", "matricula", "cpf", "curso", "periodo","11/11/11", "endereco",[])
        bolsistaprojeto = BolsistaProjeto("01-01-01", "01-01-01", "cargo", "setor", bolsista, projeto)
        projeto.inserirBolsistaProjeto(bolsistaprojeto)
        (bolsistaprojeto in projeto.listadebolsistaprojeto) |should| equal_to(True)     

    def it_inserir_lista_pesquisador(self):   
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        pesquisador = Pesquisador(1, "nome", "cpf", 222222, "endereco", "email", projeto)
        projeto.inserirPesquisador(pesquisador)
        (pesquisador in projeto.listadepesquisador) |should| equal_to(True)  

    def it_verificar_lista_pesquisador(self):   
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        pesquisador = Pesquisador(1, "nome", "cpf", 222222, "endereco", "email", projeto)
        projeto.inserirPesquisador(pesquisador)
        projeto.verificarPesquisador(pesquisador) |should| equal_to(True) 
    

class EditalSpec(unittest.TestCase):
    def it_creates_a_edital_object(self):
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        edital = Edital(1, "nome", "12-12-12", "12-13-14", projeto)
        edital.codigo |should| equal_to(1)
        edital.nome |should| equal_to("nome")
        edital.datadeinicio |should| equal_to("12-12-12")
        edital.datadetermino |should| equal_to("12-13-14")
        edital.projeto |should| equal_to(projeto)
     
class PesquisadorSpec(unittest.TestCase):
    def it_creates_a_pesquisador_object(self):
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        pesquisador = Pesquisador(1, "nome", "cpf", 222222, "endereco", "email", projeto)
        pesquisador.codigo |should| equal_to(1)
        pesquisador.nome |should| equal_to("nome")
        pesquisador.cpf |should| equal_to("cpf")
        pesquisador.telefone |should| equal_to(222222)
        pesquisador.endereco |should| equal_to("endereco")
        pesquisador.email |should| equal_to("email")
        pesquisador.projeto |should| equal_to(projeto)

class AvaliadorProjetoSpec(unittest.TestCase):
    def it_creates_a_avaliadorprojeto_object(self):
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        avaliador = Avaliador(1, "nome", [])
        avaliadorprojeto = AvaliadorProjeto("01-01-01", "02-02-02", "parecer", 10, avaliador, projeto)
        avaliadorprojeto.datacomeco |should| equal_to("01-01-01")
        avaliadorprojeto.dataentrega |should| equal_to("02-02-02")
        avaliadorprojeto.parecer |should| equal_to("parecer")
        avaliadorprojeto.nota |should| equal_to(10)
        avaliadorprojeto.avaliador |should| equal_to(avaliador)
        avaliadorprojeto.projeto |should| equal_to(projeto)

class IntegranteProjetoSpec(unittest.TestCase):
    def it_creates_a_integranteprojeto_object(self):
        integrante = Integrante(1, "nome", "cpf", 222222, "endereco", "email",[]) 
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])       
        integranteprojeto = IntegranteProjeto("01-01-01", "02-02-02", "cargo", "setor", projeto, integrante)
        integranteprojeto.datainicio |should| equal_to("01-01-01")
        integranteprojeto.datafim |should| equal_to("02-02-02")
        integranteprojeto.cargo |should| equal_to("cargo")
        integranteprojeto.setor |should| equal_to("setor")
        integranteprojeto.projeto |should| equal_to(projeto)
        integranteprojeto.integrante |should| equal_to(integrante)



class BolsistaProjetoSpec(unittest.TestCase):
    def it_creates_a_bolsistaprojeto_object(self):
        projeto = Projeto(1, "titulo", "relatorio", "11-11-11", "resumo", "situacao", [], [], [], [])
        bolsista = Bolsista(1, "nome", 1234, "cpf", "curso", 1, "01-01-01", "endereco",[])
        bolsistaprojeto = BolsistaProjeto("01-01-01", "01-01-01", "cargo", "setor", bolsista, projeto)
        bolsistaprojeto.datainicio |should| equal_to("01-01-01")
        bolsistaprojeto.datafim |should| equal_to("01-01-01")
        bolsistaprojeto.cargo |should| equal_to("cargo")
        bolsistaprojeto.setor |should| equal_to("setor")
        bolsistaprojeto.bolsista |should| equal_to(bolsista)
        bolsistaprojeto.projeto |should| equal_to(projeto)
  
