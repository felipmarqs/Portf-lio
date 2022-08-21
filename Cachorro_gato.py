
class cachorro:
    def __init__(self,nome,raca,cor):
        self.nome = nome 
        self.raca = raca 
        self.cor = cor

    def latir(self):
        return f'{self.nome} está latindo.'
    
    def andar(self):
        return f'{self.nome} está andando.'
    
    def fazer_festa(self):
        return f'{self.nome} está fazendo festa.'

class Gato:
    def __init__(self,nome,raca,cor):
        self.nome = nome 
        self.raca = raca 
        self.cor = cor
    
    def miar(self):
        return 'meow meow'
    
    def andar(self):
        return f'{self.nome} está desfilando...'

    def brincar(self, brinquedo ='novelo'):
        return f'{self.nome} está brincando com {self.brinquedo}'
