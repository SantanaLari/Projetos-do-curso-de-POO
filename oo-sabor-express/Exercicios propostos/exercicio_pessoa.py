class Pessoa:

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'Nome: {self.nome} |Idade: {self.idade} |Profissão: {self.profissao}'
    
    def aniversario(self):
        self.idade += 1
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'
    
pessoa1 = Pessoa('Ana', 25, 'Médica')
print(pessoa1)
pessoa1.aniversario()
print(pessoa1)
print(pessoa1.saudacao)