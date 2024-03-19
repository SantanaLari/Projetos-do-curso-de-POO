print('================== Exercicio 1 ==================')
# Solicite ao usuário que insira um número e, em seguida, use uma estrutura
# if else para determinar se o número é par ou ímpar
numero = int(input('Insira um número: '))

if numero % 2 == 0:
    print('Par')
else:
    print('Impar')

print('================== Exercicio 2 ==================')
# Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else
# para classificar a idade em categorias de acordo com as seguintes condições
# criança: 0 a 12 anos; adolescente: 13 a 18 anos; adulto: acima de 18 anos.
idade = int(input('Insira sua idade: '))

if idade >= 0 and idade <= 12:
    print('Criança')
elif idade >= 13 and idade <= 18:
    print('Adolescente')
elif idade > 18:
    print('Adulto')
else:
    print('Valor inválido!')

print('================== Exercicio 3 ==================')
# Solicite um nome de usuário e uma senha e usa uma estrutura if else para verificar
# se o nome de usuário e a senha fornecidos correspondem aos valores esperados
# determinados por você
usuario = input('Digite o nome de usuario: ')
senha = input('Digite a senha:')

if usuario == 'Ana' and senha == 'ana123':
    print('Usuário e senha corretos')
else:
    print('Usuário ou senha incorreto')

print('================== Exercicio 4 ==================')
# Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma
# estrutura if elif else para determinar em qual quadrante do plano cartesiano
# o ponto se encontra de acordo com as seguintes condições:
# Primeiro quadrante: os valores de x e y devem ser maiores que zero
# Segundo quadrante: o valor de x é menor que zero e o valor de y é maior que zero
# Terceiro quadrante: os valores de x e y devem ser menores que zero
# Quarto quadrante: o valor de x é maior que zero e o valor de y é menor que zero
# Caso contrário: o ponto está localizado no eixo ou origem
x = int(input('Valor de x: '))
y = int(input('Valor de y: '))

if x > 0:
    if y > 0: # x > 0 e y > 0
        print('Primeiro Quadrante')
    else: # x > 0 e y < 0
        print('Quarto Quadrante')
elif x < 0:
    if y > 0: # x < 0 e y > 0
        print('Segundo Quadrante')
    else: # x < 0 e y < 0
        print('Terceiro Quadrante')
else:
    print('O ponto está localizado no eixo ou na origem')