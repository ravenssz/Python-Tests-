import unittest
from should_dsl import should
from exer05 import *

class UsuarioSpec(unittest.TestCase):
    
    def it_creates_a_usuario_object(self):
    
        usuario = Usuario(1, "nome", 10, 100, 10, "A", 300, "M", 200, 10,20, 10,20,10, 10, [],[])
        usuario.codigo |should| equal_to(1)
        usuario.nome |should| equal_to("nome")
        usuario.peso |should| equal_to(10)
        usuario.altura |should| equal_to(100)
        usuario.gordura_corporal |should| equal_to(10)
        usuario.nivel_atividade_fisica |should| equal_to("A")
        usuario.calorias_a_consumir |should| equal_to(300)
        usuario.sexo |should| equal_to("M")
        usuario.valor_metabolico |should| equal_to(200)
        usuario.massa_magra |should| equal_to(10)
        usuario.peso_gordura |should| equal_to(20)
        usuario.peso_gordura_ideal |should| equal_to(10)
        usuario.peso_ideal |should| equal_to(20)
        usuario.peso_a_perder |should| equal_to(10)
        usuario.idade |should| equal_to(10)     
        usuario.listadeusuariotreino |should| equal_to([])
        usuario.listaderefeicao |should| equal_to([])

    def it_inserir_lista_refeicao_projeto(self):
        alimentos = Alimentos(1, "nome","B",10,10,10,10,10,[])
        usuario = Usuario(1, "nome", 10, 100, 10, "A", 300, "M", 200, 10,20, 10,20,10, 10, [],[])
        refeicao = Refeicao(1, "nome", 1, "20:20", usuario, alimentos)
        usuario.inserirRefeicao(refeicao)
        (refeicao in usuario.listaderefeicao) |should| equal_to(True)

    def it_verificar_lista_refeicao_projeto(self):
        alimentos = Alimentos(1, "nome","B",10,10,10,10,10,[])
        usuario = Usuario(1, "nome", 10, 100, 10, "A", 300, "M", 200, 10,20, 10,20,10, 10, [],[])
        refeicao = Refeicao(1, "nome", 1, "20:20", usuario, alimentos)
        usuario.inserirRefeicao(refeicao)
        usuario.verificarRefeicao(refeicao) |should| equal_to(True)

    def it_inserir_lista_usuario_treino_projeto(self):
        usuario = Usuario(1, "nome", 10, 100, 10, "A", 300, "M", 200, 10,20, 10,20,10, 10, [],[])
        treino = Treino(1, "nome", 10, 234,"12:21", "23-12-12",[],[])
        usuariotreino = UsuarioTreino(1, usuario, treino)
        usuario.inserirUsuarioTreino(usuariotreino)
        (usuariotreino in usuario.listadeusuariotreino) |should| equal_to(True)

    def it_verificar_lista_usuario_treino_projeto(self):
        usuario = Usuario(1, "nome", 10, 100, 10, "A", 300, "M", 200, 10,20, 10,20,10, 10, [],[])
        treino = Treino(1, "nome", 10, 234,"12:21", "23-12-12",[],[])
        usuariotreino = UsuarioTreino(1, usuario, treino)
        usuario.inserirUsuarioTreino(usuariotreino)
        usuario.verificarUsuarioTreino(usuariotreino) |should| equal_to(True)

class AlimentosSpec(unittest.TestCase):

    def it_creates_a_alimentos_object(self):

        alimentos = Alimentos(1, "nome","B",10,10,10,10,10,[])
        alimentos.codigo |should| equal_to(1)
        alimentos.nome |should| equal_to("nome")
        alimentos.categoria |should| equal_to("B")
        alimentos.quantidade |should| equal_to(10)
        alimentos.calorias |should| equal_to(10)
        alimentos.proteinas |should| equal_to(10)
        alimentos.carboidratos |should| equal_to(10)
        alimentos.gorduras |should| equal_to(10)
        alimentos.listaderefeicao |should| equal_to([])

    def it_inserir_lista_refeicao_projeto(self):
        alimentos = Alimentos(1, "nome","B",10,10,10,10,10,[])
        usuario = Usuario(1, "nome", 10, 100, 10, "A", 300, "M", 200, 10,20, 10,20,10, 10, [],[])
        refeicao = Refeicao(1, "nome", 1, "20:20", usuario, alimentos)
        alimentos.inserirRefeicao(refeicao)
        (refeicao in alimentos.listaderefeicao) |should| equal_to(True)

    def it_verificar_lista_refeicao_projeto(self):
        alimentos = Alimentos(1, "nome","B",10,10,10,10,10,[])
        usuario = Usuario(1, "nome", 10, 100, 10, "A", 300, "M", 200, 10,20, 10,20,10, 10, [],[])
        refeicao = Refeicao(1, "nome", 1, "20:20", usuario, alimentos)
        alimentos.inserirRefeicao(refeicao)
        alimentos.verificarRefeicao(refeicao) |should| equal_to(True)

class RefeicaoSpec(unittest.TestCase):
    
    def it_creates_a_refeicao_object(self):
        alimentos = Alimentos(1, "nome","B",10,10,10,10,10,[])
        usuario = Usuario(1, "nome", 10, 100, 10, "A", 300, "M", 200, 10,20, 10,20,10, 10, [],[])
        refeicao = Refeicao(1, "nome", 1, "20:20", usuario, alimentos)  
        refeicao.codigo |should| equal_to(1)
        refeicao.nome |should| equal_to("nome")
        refeicao.total_calorias |should| equal_to(1)
        refeicao.horario |should| equal_to("20:20")
        refeicao.usuario |should| equal_to(usuario)
        refeicao.alimentos |should| equal_to(alimentos)   

class HistoricoSpec(unittest.TestCase):
    def it_creates_a_historico_object(self):
        usuario = Usuario(1, "nome", 10, 100, 10, "A", 300, "M", 200, 10,20, 10,20,10, 10, [],[])
        historico = Historico(1,1,1,"A",1, usuario)
        historico.codigo |should| equal_to(1)
        historico.peso_atual |should| equal_to(1)
        historico.peso_perdido |should| equal_to(1)
        historico.situacao |should| equal_to("A")
        historico.saldo_calorias |should| equal_to(1)
        historico.usuario |should| equal_to(usuario)

class TreinoSpec(unittest.TestCase):
    def it_creates_a_treino_object(self):
        treino = Treino(1, "nome", 10, 234,"12:21", "23-12-12",[],[])
        treino.codigo |should| equal_to(1)
        treino.nome |should| equal_to("nome")
        treino.total_calorias_gastas |should| equal_to(10)
        treino.tempo_total |should| equal_to(234)
        treino.horario |should| equal_to("12:21")
        treino.data |should| equal_to("23-12-12")
        treino.listadeusuariotreino |should| equal_to([])
        treino.listatreinoexercicio |should| equal_to([])

    def it_inserir_lista_usuario_treino_projeto(self):
        usuario = Usuario(1, "nome", 10, 100, 10, "A", 300, "M", 200, 10,20, 10,20,10, 10, [],[])
        treino = Treino(1, "nome", 10, 234,"12:21", "23-12-12",[],[])
        usuariotreino = UsuarioTreino(1, usuario, treino)
        treino.inserirUsuarioTreino(usuariotreino)
        (usuariotreino in treino.listadeusuariotreino) |should| equal_to(True)

    def it_verificar_lista_usuario_treino_projeto(self):
        usuario = Usuario(1, "nome", 10, 100, 10, "A", 300, "M", 200, 10,20, 10,20,10, 10, [],[])
        treino = Treino(1, "nome", 10, 234,"12:21", "23-12-12",[],[])
        usuariotreino = UsuarioTreino(1, usuario, treino)
        treino.inserirUsuarioTreino(usuariotreino)
        treino.verificarUsuarioTreino(usuariotreino) |should| equal_to(True)

    def it_inserir_lista_treino_exercicios_projeto(self):
        treino = Treino(1, "nome", 10, 234,"12:21", "23-12-12",[],[])
        exercicios = Exercicios(1,"nome",22,12,12,23,[])
        treinoexercicios = TreinoExercicios(1, exercicios, treino)
        treino.inserirTreinoExercicios(treinoexercicios)

        (treinoexercicios in treino.listatreinoexercicio) |should| equal_to(True)
    def it_verificar_lista_treino_exercicios_projeto(self):
        treino = Treino(1, "nome", 10, 234,"12:21", "23-12-12",[],[])
        exercicios = Exercicios(1,"nome",22,12,12,23,[])
        treinoexercicios = TreinoExercicios(1, exercicios, treino)
        treino.inserirTreinoExercicios(treinoexercicios)
        treino.verificarTreinoExecicios(treinoexercicios) |should| equal_to(True)


class UsuarioTreinoSpec(unittest.TestCase):
    def it_creates_a_usuario_treino_object(self):
        usuario = Usuario(1, "nome", 10, 100, 10, "A", 300, "M", 200, 10,20, 10,20,10,10, [],[])
        treino = Treino(1, "nome", 10, 234,"12:21", "23-12-12",[])
        usuariotreino = UsuarioTreino(1, usuario, treino)
        usuariotreino.codigo |should| equal_to(1)
        usuariotreino.usuario |should| equal_to(usuario)
        usuariotreino.treino |should| equal_to(treino)

class ExerciciosSpec(unittest.TestCase):
    def it_creates_a_exercicios_object(self):
        exercicios = Exercicios(1,"nome",22,12,12,23,[])
        exercicios.codigo |should| equal_to(1)
        exercicios.nome |should| equal_to("nome")
        exercicios.calorias_gastas |should| equal_to(22)
        exercicios.numero_series |should| equal_to(12)
        exercicios.tempo_descanso |should| equal_to(12)
        exercicios.tempo_exercicio |should| equal_to(23)
        exercicios.lista_treinoexercicios |should| equal_to([])

    def it_inserir_lista_treino_exercicios_projeto(self):
        treino = Treino(1, "nome", 10, 234,"12:21", "23-12-12",[],[])
        exercicios = Exercicios(1,"nome",22,12,12,23,[])
        treinoexercicios = TreinoExercicios(1, exercicios, treino)
        exercicios.inserirTreinoExercicios(treinoexercicios)
        (treinoexercicios in exercicios.lista_treinoexercicios) |should| equal_to(True)

    def it_verificar_lista_treino_exercicios_projeto(self):
        treino = Treino(1, "nome", 10, 234,"12:21", "23-12-12",[],[])
        exercicios = Exercicios(1,"nome",22,12,12,23,[])
        treinoexercicios = TreinoExercicios(1, exercicios, treino)
        exercicios.inserirTreinoExercicios(treinoexercicios)
        exercicios.verificarTreinoExecicios(treinoexercicios) |should| equal_to(True)

class TreinoExerciciosSpec(unittest.TestCase):
    def it_creates_a_treino_exercicios_object(self):
        treino = Treino(1, "nome", 10, 234,"12:21", "23-12-12",[],[])
        exercicios = Exercicios(1,"nome",22,12,12,23,[])
        treinoexercicios = TreinoExercicios(1, exercicios, treino)
        treinoexercicios.codigo |should| equal_to(1)
        treinoexercicios.treino |should| equal_to(treino)
        treinoexercicios.exercicios |should| equal_to(exercicios)

        
        

