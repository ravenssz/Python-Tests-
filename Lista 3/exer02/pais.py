
class Pais:
    
    def __init__(self, nome, capital, dimensao, listapaises=[]):
        self.nome = nome
        self.capital = capital
        self.dimensao = dimensao
        self.listapaises = listapaises

    def inserirPais(self,pais):
        if self.comparar_pais(pais) == False:        
            self.listapaises.append(pais)


    def comparar_pais(self, pais):
        if (self.nome == pais.nome) and (self.capital == pais.capital):  
            return True
        return False

    def pais_em_comum(self, pais):
        if pais.listapaises == self.listapaises:    
            return True
        return False

    def verificar_paises_iguais(self, pais):
        iguais = []
        for x in pais.listapaises:
            if x in self.listapaises:
                iguais.append(x)
        return iguais
                
 
    
