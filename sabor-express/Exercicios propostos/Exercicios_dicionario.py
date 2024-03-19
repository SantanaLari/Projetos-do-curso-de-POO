def titulo_exercicio(num_exercicio):
    print('=' * 40, f'Exercicio {num_exercicio}', '=' * 40)

# 1- Crie um dicionario representando informações sobre uma pessoa, como nome,
# idade e cidade
titulo_exercicio(1)
dados = {'nome':'Ana', 'idade':25, 'cidade':'São Paulo'}
print(dados)

# 2- Utilizando o dicionario criado no item 1:
# Modifique o valor de um dos itens no dicionario
# Adicione um campo de profissão para essa pessoa
# Remova um item do dicionário
titulo_exercicio(2)
dados.update({'idade':27})
print('Update: ', dados)

dados['profissao'] = 'Dentista'
print('Adicao de profissão: ', dados)

del dados['cidade']

print('Cidade removida: ', dados)

# 3- Crie um dicionario utilizando para representar números e seus quadrados de 1 a 5
titulo_exercicio(3)
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

# 4- Crie um dicionario e verifique se uma chave especifica existe dentro desse dicionario
titulo_exercicio(4)
filmes = {'nome':'O mágico de Oz', 'data':1939}

if 'genero' in filmes:
    print("A chave 'genero' existe no dicionario 'Filme'")
else:
    print("A chave 'genero' não existe no dicionario 'Filme'")

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando
# um dicionário
titulo_exercicio(5)
frase = "O rato roeu a roupa do rei de roma em roma"
contagem = {}
palavras = frase.split()
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(contagem)