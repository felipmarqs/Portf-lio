class ContaCorrente:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo
        self.__extrato = []

    def consultar_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        self.__saldo += valor
        self.__extrato.append(f'(+){valor:.2f}')

    def sacar(self, valor):
        if valor > self.__saldo:
            return 'Saldo insuficiente.'
        self.__saldo -= valor
        self.__extrato.append(f'(-){valor:.2f}')
    
    def transferir(self,destino,valor):
        self.sacar(valor)
        destino.depositar(valor)
        return 'Transferência realizada com sucesso.'
    
    def consultar_extrato(self):
        print('-=' * 10, 'EXTRATO', '-=' * 10)
        print(self.titular)
        for mov in self.__extrato:
            print(mov)
        print(f'Saldo: {self.consultar_saldo()}')
    
