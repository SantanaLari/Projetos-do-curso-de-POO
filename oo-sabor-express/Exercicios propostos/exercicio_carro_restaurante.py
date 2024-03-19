# exercicio 1
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    

carro1 = Carro('Chevrolet', 'Preto', 1957)


# exercicio 2,3,4
class Restaurante:
    def __init__(self, nome, categoria, capacidade, nota_avaliacao, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante1 = Restaurante('NostraFamilia', 'Italiano', 100, 5, ativo=True)
print(restaurante1)

# exercicio 5
class Cliente: 
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

cliente1 = Cliente('Lucia', 23, 'lucia123@gmail.com', 11112222)
cliente2 = Cliente('Marcos', 25, 'marcos17@gmail.com', 12345678)
cliente3 = Cliente('Carina', 28, 'carinamendes@gmail.com', 11223344)

