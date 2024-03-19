# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
print('======================== Exercicio 1 ========================')
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_nomes = ['Ana', 'Bianca', 'Carlos', 'Daniele']
lista_anos = [2001, 2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista
print('======================== Exercicio 2 ========================')
lista_frutas = ['Pêra', 'Uva', 'Maçã', 'Salada Mista']

for fruta in lista_frutas:
    print(fruta)

# 3 - Utilize um loop para calcular a soma dos números ímpares de 1 a 10
print('======================== Exercicio 3 ========================')
soma_impares = 0
for numero in range(1, 10, 2):
    soma_impares += numero

print('Soma: ', soma_impares)

# 4 - Utilize um loop para imprimir os números de 1 a 10 em ordem decrescente
print('======================== Exercicio 4 ========================')
for numero in range(10, 0, -1):
    print(numero)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para
# imprimir a tabuada desse número, indeo de 1 a 10
print('======================== Exercicio 5 ========================')
num_tabuada = 2 #int(input('Digite um número: '))

for valor in range(1, 11):
    res = num_tabuada * valor
    print(f'{num_tabuada} x {valor} = {res}')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma 
# Utilize um bloco try-except para lidar com possiveis exceções
print('======================== Exercicio 6 ========================')
lista_numeros_ex6 = [1,2,3,4,5,None,6,'a'] 
res_soma = 0 

try:
    for num in lista_numeros_ex6:
        res_soma += num
    print('Resultado: ', res_soma)
except Exception as e:
    print(f'Ocorreu um erro: {e}')
        
# 7 - Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista 
# esteja vazia
print('======================== Exercicio 7 ========================')
lista_media = [1,2,3,4,5,6]

try:
    media = sum(lista_media)/len(lista_media)
    print('Media: ', media)
except ZeroDivisionError:
    print('Lista vazia')
