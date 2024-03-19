class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self.titular} |Saldo: {self.saldo}'
    
    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    
conta1 = ContaBancaria('Jose', 1500)
conta2 = ContaBancaria('Paula', 2000)

print(f'{conta1}\n{conta2}')

conta3 = ContaBancaria('Carlos', 200)
print(f'Conta ativa? {conta3._ativo}')
ContaBancaria.ativar_conta(conta3)
print(f'Conta ativa? {conta3._ativo}')

conta4 = ContaBancaria('Julia', 500)
print(f'Titular: {conta4.titular}')

class ClienteBanco:

    clientes_lista = []

    def __init__(self, nome, cpf, data_nascimento, endereco, telefone):
        self.nome = nome 
        self._cpf = cpf 
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone
        ClienteBanco.clientes_lista.append(self)

    @property
    def cpf(self):
        cpf_ocultado = self._cpf[:3] + '.xxx.xxx-' + self._cpf[-2:]
        return cpf_ocultado

    @classmethod
    def lista_cliente(cls):
        for cliente in cls.clientes_lista:
            print(f'Nome: {cliente.nome} | CPF: {cliente.cpf}')
    
cliente1 = ClienteBanco('Carlos', '123.123.123-12', '10/02/2000', 'Rua x', '11912341234')
cliente2 = ClienteBanco('Sofia', '123.456.789-10', '10/10/1999', 'rua y', '99999-9999')
cliente3 = ClienteBanco('Bianca', '000.111.000-11', '18/06/1985', 'rua w', '8888-8888')

ClienteBanco.lista_cliente()